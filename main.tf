terraform {
    required_providers {
        azurerm = {
            source = "hashicorp/azurerm"
            version = ">= 3.8"
        }
    }
}

provider "azurerm" {
    features {}
    subscription_id = "d33b95c7-af3c-4247-9661-aa96d47fccc0"
}

data "azurerm_resource_group" "main" {
    name = "Cohort31_CriOli_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
    name = "terraformed-asp"
    location = data.azurerm_resource_group.main.location
    resource_group_name = data.azurerm_resource_group.main.name
    os_type = "Linux"
    sku_name = "B1"    
}

resource "azurerm_linux_web_app" "main" {
    name = "cristianoterraformapp"
    location = data.azurerm_resource_group.main.location
    resource_group_name = data.azurerm_resource_group.main.name
    service_plan_id = azurerm_service_plan.main.id
    
    site_config {
        application_stack {
            docker_image_name = "appsvcsample/python-helloworld"
            docker_registry_url = "https://index.docker.io"
        }
    }
}

