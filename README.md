# guance-python-spug-demo
> 项目来源：[Spug](https://github.com/openspug/spug)

[观测云](https://www.guance.com/)是一款旨在解决云计算，以及云原生时代系统为每一个完整的应用构建全链路的可观测性的云服务平台。本项目通过 Spug 系统，让您快速了解 Python 服务接入观测云的流程以及体验完整的全链路可观测性。

***

## 前提条件
[安装 DataKit Operator 和 DataKit](https://github.com/GuanceDemo/guance-datakit-demo)


## 方式一：Helm 方式手动安装
> 通过 Helm 安装至 Kubernetes 集群，适合快速安装 guance-python-spug-demo 进行演示的场景。


### 1. 安装
#### 1.1 执行安装
```shell
git clone https://github.com/GuanceDemo/guance-python-spug-demo.git
helm upgrade -i spug-server  --create-namespace --namespace spug ./deployment/helm
```

#### 1.2 访问方式
部署完成后可通过 gvb-front 的 NodePort 方式进行访问，默认端口为 30003
- 控制台页面：\<spug-node-ip>:30003
  -  账号：admin
  - 密码：admin



### 2. 卸载
```shell
helm uninstall spug-server -n spug
```

***

## 方式二：自动化打包部署
> 通过 Github Action 自动打包并安装至 Kubernetes 集群，适合对 guance-go-ginvueblog-demo 源码修改的场景。

### 1. fork 代码到自己的 Github 仓库

### 2. 创建并添加以下密钥和变量
> 创建路径：Settings --> Secrets and Variables --> Action  

New repository Secret
- `KUBECONFIG`: Kubernetes config文件，用于 Action 执行机远程操作 Kubernetes 集群
- `DOCKER_USERNAME`: 镜像仓库登陆用户名
- `DOCKER_PASSWORD`: 镜像仓库登陆密码
- `GUANCE_ACCESS_TOKEN`: 观测云 Key ID，创建方式：[API Key](https://docs.guance.com/management/api-key/)

New repository Variable
- `DOCKER_REGISTRY`: 镜像仓库地址，如 pubrepo.guance.com
- `DOCKER_NAMESPACE`: 镜像仓库项目名，如 demo
- `GUANCE_REGION`: 观测云 region，可选项：[terraform-provider-guance](https://github.com/GuanceCloud/terraform-provider-guance)

> 配置后镜像地址：$DOCKER_REGISTRY/$DOCKER_NAMESPACE/demo:latest


### 3. 触发自动打包流水线
> 手动触发路径：Action --> Build and push gvb backend demo images/Build and push gvb ui demo images --> Run Workflow

自动打包流水线会自动打包 Gin-Vue-Blog 的前端和后端镜像并推送至镜像仓库, 可通过修改 src 下任意文件或手动方式进行触发。

- `Build and push gvb ui demo images`: 前端 CI 流水线
- `Build and push gvb backend demo images`: 后端 CI 流水线

### 4. 触发自动部署流水线 
自动部署流水线通过手动触发进行部署。
- `Deploy gvb demo on kubernetes`: CD 流水线

### 5. 访问方式
部署完成后可通过 gvb-front 的 NodePort 方式进行访问，默认端口为 30002
- 博客系统页面：\<gvb-front-node-ip>:30002
- 博客后台页面: \<gvb-front-node-ip>:30002/admin
  -  账号：admin
  - 密码：123456

### 6. 卸载
destroy 进行卸载
- `Uninstall gvb demo on kubernetes`: 从 Kubernetes 集群删除