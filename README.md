

# BookRoom Agents
> 智能助手API
>
> About API for Agents.


## 使用说明
### 支持OpenAI调用方式
``` 

Coming soon...

```

### 部署后访问以下地址查看API文档 
#### 1. **Swagger UI(Docs)**
`http://localhost:15230/docs`

#### 2. **ReDoc**
`http://localhost:15230/redoc`

## 🛠️ 安装
```bash
# 克隆 GitHub 仓库
git clone https://github.com/sndraw/bookroom-agents.git

# 进入项目目录
cd bookroom-agents

# 如果你还没有安装 uv，请先安装（可能需要需要设置uv到系统环境变量）
pip install uv

# 创建虚拟环境并安装依赖，支持 Python 3.11
uv venv .venv --python=3.11

# 激活虚拟环境
## macOS/Linux
source .venv/bin/activate
## Windows
.venv\Scripts\activate

# 安装所有依赖
uv pip install -e .

# 完成后退出虚拟环境
deactivate
```

## 🚀 启动
### **设置环境变量**
在项目根目录下复制``.env.example并重命名为 .env，并根据需要修改环境变量。

例如：
   
```bash
API_KEY=your_api_key_here # 你的 API 密钥，如果没有可以不填
```
### **启动服务**
```bash
# 正常运行模式
uv run -m bookroom_agents.server

# 开启调试模式，代码修改后自动重启服务
uv run -m bookroom_agents.server --reload

```


## Docker打包
### 1. 登录镜像仓库（可选）
```bash
docker login -u username <IP:port>/<repository>
```
### 2. 构建镜像

#### make命令（参数可选）
注：Makefile中定义了build-push-all目标，可以一次性构建并推送镜像
```bash
make build-push-all REGISTRY_URL=<IP:port>/<repository> IMAGE_NAME=sndraw/bookroom-agents IMAGE_VERISON=0.0.1
```

## 截图展示
``` 

Coming soon...

```