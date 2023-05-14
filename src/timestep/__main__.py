import typer

from constructs import Construct
from cdktf import App, TerraformOutput, TerraformProvider, TerraformStack

from imports.multipass.provider import MultipassProvider as MultipassTerraformProvider
from imports.multipass.instance import Instance as MultipassTerraformResource
from imports.multipass.data_multipass_instance import DataMultipassInstance as MultipassTerraformDataSource

class MainTerraformStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, target: str):
        super().__init__(scope, id)

        provider = MultipassTerraformProvider(
            id=f"{id}-{target}-provider",
            scope=self,
        )
        assert isinstance(provider, TerraformProvider)

        import os
        cwd = os.getcwd()
        print(f"cwd: {cwd}")

        cloudinit_file = f"{cwd}/src/timestep/envs/env/cloud.yaml"

        resource = MultipassTerraformResource(
            cloudinit_file=cloudinit_file,
            cpus=2,
            disk="40G",
            id=f"{id}-{target}-resource",
            image="22.04", # "ros2-humble",
            # image="ros2-humble",
            # memory="4G",
            name=f"{id}",
            provider=provider,
            scope=self,
        )
        assert isinstance(resource, MultipassTerraformResource)

        data_source = MultipassTerraformDataSource(
            id=f"{id}-{target}-data_source",
            name=resource.name,
            provider=provider,
            scope=self,
        )
        assert isinstance(data_source, MultipassTerraformDataSource)

        output = TerraformOutput(
            id=f"{id}-{target}-ipv4-output",
            value=data_source.ipv4,
            scope=self,
        )
        # print(f"output: {output}")

def main(app_name: str="timestep", env: str="localhost"):
    print(f"Running {app_name} in {env} mode")

    app = App()

    MainTerraformStack(scope=app, id=app_name, target=env)

    app.synth()


if __name__ == "__main__":
    typer.run(main)
