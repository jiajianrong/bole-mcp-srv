在目标服务器（安装了openclaw）上：


```

cd /root
git clone git@gitee.com:bona-dev/bole-mcp-srv.git

cd /root/bole-mcp-srv
cp ./SKILL.md {openclaw_skills_dir}

openclaw gateway restart

```