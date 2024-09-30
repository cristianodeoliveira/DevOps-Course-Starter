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
            docker_image_name = "cristianodeoliveira/todo-app:prodlatest"
            docker_registry_url = "https://index.docker.io"
        }
    }
        app_settings = {
        FLASK_APP = "todo_app/app"
        FLASK_DEBUG = "true"
        SECRET_KEY = "secret-key"
        MONGODB_CONNECTION_STRING = azurerm_cosmosdb_account.main.primary_mongodb_connection_string
        MONGODB_DB_NAME = "todoappmongodb"
        MONGODB_COLLECTION_NAME = "todo_entries"
        WEBSITES_PORT = "5000"
    }
}



resource "azurerm_cosmosdb_account" "main" {
  name                = "cristiano-terraform-db"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  capabilities {
    name = "EnableServerless"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  geo_location {
    location          = "uksouth"
    failover_priority = 0
  }

  lifecycle { 
    prevent_destroy = true 
  }
}