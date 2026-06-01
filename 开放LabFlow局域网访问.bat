@echo off
chcp 65001 > nul

echo 正在配置 LabFlow 局域网访问...
echo.

net session >nul 2>&1
if %errorlevel% neq 0 (
  echo 请右键点击本文件，选择“以管理员身份运行”。
  echo.
  pause
  exit /b 1
)

netsh advfirewall firewall delete rule name="LabFlow 8080" >nul 2>&1
netsh advfirewall firewall add rule name="LabFlow 8080" dir=in action=allow protocol=TCP localport=8080 profile=private >nul

if %errorlevel% equ 0 (
  echo 已放行 TCP 8080 端口。
  echo.
  echo 其他电脑请访问：
  echo http://172.16.1.71:8080
) else (
  echo 配置失败，请检查 Windows 防火墙或管理员权限。
)

echo.
pause
