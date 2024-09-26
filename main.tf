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
}

data "azurerm_resource_group" "main" {
    name = "Cohort31_CriOli_ProjectExercise"
}