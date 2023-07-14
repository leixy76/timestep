from cdktf import (
    CloudBackend,
    LocalBackend,
    NamedCloudWorkspace,
    TerraformStack,
)
from constructs import Construct

from timestep.conf.blocks import AppConfig
from timestep.infra.stacks.main.constructs.cloud_init_config.construct import (
    CloudInitConfigConstruct,
)
from timestep.infra.stacks.main.constructs.cloud_instance.construct import (
    CloudInstanceConstruct,
)
from timestep.infra.stacks.main.constructs.cloud_instance_domain.construct import (
    CloudInstanceDomainConstruct,
)
from timestep.infra.stacks.main.constructs.domain_name_registrar.construct import (
    DomainNameRegistrarConstruct,
)


class MainStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, config: AppConfig) -> None:
        super().__init__(scope, id)

        stack_id: str = config.variables.get("primary_domain_name")

        self.cloud_init_config_construct: CloudInitConfigConstruct = (
            CloudInitConfigConstruct(
                config=config,
                id="cloud_init_config_construct",
                scope=self,
            )
        )

        self.cloud_instance_construct: CloudInstanceConstruct = CloudInstanceConstruct(
            cloud_init_config_construct=self.cloud_init_config_construct,
            config=config,
            id="cloud_instance_construct",
            scope=self,
        )

        self.cloud_instance_domain_construct: CloudInstanceDomainConstruct = (
            CloudInstanceDomainConstruct(  # noqa: E501
                cloud_instance_construct=self.cloud_instance_construct,
                config=config,
                id="cloud_instance_domain_construct",
                scope=self,
            )
        )

        self.domain_name_registar_construct: DomainNameRegistrarConstruct = (
            DomainNameRegistrarConstruct(  # noqa: E501
                config=config,
                id="domain_name_registar_construct",
                scope=self,
            )
        )

        if (
            config.variables.get("cloud_instance_provider")
            == CloudInitConfigConstruct.CloudInstanceProvider.MULTIPASS
        ):
            LocalBackend(
                path=f"terraform.{stack_id}.tfstate",
                scope=self,
                workspace_dir=None,
            )

        else:
            CloudBackend(
                hostname=config.variables.get("tf_hostname"),
                organization=config.variables.get("tf_organization"),
                scope=self,
                token=config.secrets.get_secret_value().get("tf_api_token"),
                workspaces=NamedCloudWorkspace(config.variables.get("tf_workspace")),
            )