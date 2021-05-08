<template>
  <div>
    <AccountHeader></AccountHeader>
    <el-row>
      <AccountLoginOrRegisterHeaderImage></AccountLoginOrRegisterHeaderImage>
      <el-col :offset="6" :span="12">
        <el-row style="margin-top: 20px">
          <el-col>
            <el-col style="margin-bottom: 30px">


              <el-divider>
                <h1>
                  登录
                </h1>
              </el-divider>
            </el-col>


          </el-col>
        </el-row>

        <el-col :span="12" style="border-right: 0px solid rgb(220,223,230);text-align: center">

          <el-image src="/static/img/binaryCode.png"></el-image>
          <!--          <el-image src="https://s1.hdslb.com/bfs/static/passport/static/img/2233login.af9c53d.png"></el-image>-->
          <div
                  style="background-image: url(https://s1.hdslb.com/bfs/static/passport/static/img/2233login.af9c53d.png);height: 200px;padding-top: 1px">
            <div style="margin-top: 20px;font-size: 16px">扫描二维码登录</div>
            <div style="font-size: 12px;margin-top: 10px">请使用 <span class="primary">哔哩哔哩客户端</span></div>
            <div style="font-size: 12px;margin-top: 10px">扫码登录</div>
            <div style="font-size: 12px;margin-top: 10px">或者扫码下载APP</div>
          </div>
        </el-col>

        <el-col :span="10" :offset="0" style="border-left: 1px solid rgb(220,223,230);padding-left: 20px">
          <el-form>
            <el-form-item>
              <el-button type="text" @click="active='password_login'"
                         :style="{color: active==='password_login'? 'rgb(2,167,222)' :''}">
                密码登录
              </el-button>
              <el-button type="text" @click="active=''"
                         :style="{color: active!=='password_login'? 'rgb(2,167,222)' :''}">
                短信登录
              </el-button>
            </el-form-item>
            <el-form-item>
              <el-input placeholder="你的手机号/邮箱" v-model="form.phoneOrEmail"></el-input>
            </el-form-item>
            <el-form-item>
              <el-input placeholder="密码" @keydown.native.enter="toLogin" v-model="form.password"></el-input>

            </el-form-item>
            <div style="font-size: 10px">
              <el-checkbox v-model="memory">记住我</el-checkbox>
              <span style="color: rgb(187,187,187)">
               不是自己的电脑上不要勾选此项
              </span>
              <span style="float: right">
                <router-link class="primary" to="">
                无法验证?
              </router-link>
              <router-link class="primary" to="">
                忘记密码?
              </router-link>
              </span>
            </div>
            <el-form-item style="margin-top: 20px">
              <el-button style="width: 45%;color: white" type="primary" @click="toLogin">登录</el-button>
              <el-button style="width: 45%;float: right" @click="toRegister"> 注册</el-button>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col style="text-align: center;font-size: 10px">
          登录即代表你同意
          <router-link class="primary" to="">
            用户协议
          </router-link>
          和
          <router-link class="primary" to="">
            隐私政策
          </router-link>
        </el-col>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    import AccountHeader from "@/views/account/AccountHeader";
    import AccountLoginOrRegisterHeaderImage from "@/views/account/AccountLoginOrRegisterHeaderImage";

    export default {
        name: "AccountLogin",
        components: {
            AccountLoginOrRegisterHeaderImage,
            AccountHeader
        },
        data: () => ({
            memory: true,
            active: 'password_login',
            form: {
                phoneOrEmail: '',
                password: ''
            },
            getter: null,
        }),
        methods: {
            toLogin() {
                this.$store.dispatch('user/login', this.form)
                    .then(() => this.$store.dispatch('user/getInfo'))


            },
            toRegister() {
                this.$router.push({
                    path: '/register'
                })
            }
        },
        mounted() {

        }
    }
</script>

<style scoped>

</style>
