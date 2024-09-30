output "webapp_url" {
    value = "https://${azurerm_linux_web_app.main.default_hostname}"
}

output "webhook_url" {
    sensitive = true
    value = "https://${azurerm_linux_web_app.main.site_credential[0].name}:${azurerm_linux_web_app.main.site_credential[0].password}@${azurerm_linux_web_app.main.name}.scm.azurewebsites.net/docker/hook"
}