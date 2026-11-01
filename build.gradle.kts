import com.pswidersk.gradle.python.uv.UvTask

plugins {
    id("com.pswidersk.python-uv-plugin") version "0.4.33"
}

tasks {

    register<UvTask>("uvInfo") {
        description = "List UV tool info"
        args = listOf("help")
    }
    val uvEnvInstall = register<UvTask>("uvEnvInstall") {
        description = "UV environment install"
        args = listOf("venv")
    }

    val uvInstall = register<UvTask>("uvInstall") {
        description = "UV tool install"
        val requirementsFile = projectDir.resolve("requirements.txt").path
        args = listOf("pip", "install", "-r", requirementsFile)
        dependsOn(uvEnvInstall)
    }

    register<UvTask>("pandocRun") {
        description = "Generate output files"
        args = listOf("run", "generate.py")
        dependsOn(uvInstall)
    }

}
