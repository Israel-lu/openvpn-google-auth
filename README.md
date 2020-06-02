# openvpn-google-auth
google 二次验证脚本
使用python3
##
openvpn server.conf配置文件添加
  auth-user-pass-verify /etc/openvpn/auth.py via-env
  client-cert-not-required
  username-as-common-name
  script-security 3
  reneg-sec 0
##
clent.ovpn 添加
  auth-user-pass
  auth-nocache
  reneg-sec 0
