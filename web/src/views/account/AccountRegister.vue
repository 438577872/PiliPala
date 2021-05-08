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
                  <!--                  登录-->
                  注册
                </h1>
              </el-divider>
            </el-col>

          </el-col>
        </el-row>


        <el-col :span="11" :offset="6" style="border-left: 0px solid rgb(220,223,230);padding-left: 20px">
          <el-form>
            <!--            <el-form-item>-->
            <!--              <el-button type="text" @click="active='password_login'" :style="{color: active==='password_login'? 'rgb(2,167,222)' :''}">-->
            <!--                密码登录-->
            <!--              </el-button>-->
            <!--              <el-button type="text" @click="active=''" :style="{color: active!=='password_login'? 'rgb(2,167,222)' :''}" >-->
            <!--                短信登录-->
            <!--              </el-button>-->
            <!--            </el-form-item>-->
            <el-form-item>
              <el-input placeholder="昵称" v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item>
              <el-input placeholder="密码(6-16个字符组成/区分大小写)" v-model="form.password"></el-input>

            </el-form-item>
            <el-form-item>
              <el-input placeholder="填写手机号" v-model="form.phone">
                <el-select slot="prepend" v-model="val" style="width: 100px" placeholder="请选择">
                  <el-option
                      v-for="item in list"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                  </el-option>
                </el-select>
                <!--                <el-select>-->
                <!--                  <el-option></el-option>-->
                <!--                </el-select>-->
              </el-input>
            </el-form-item>
            <!--            <div style="font-size: 10px">-->
            <!--              <el-checkbox v-model="memory">记住我</el-checkbox>-->
            <!--              <span style="color: rgb(187,187,187)">-->
            <!--               不是自己的电脑上不要勾选此项-->
            <!--              </span>-->
            <!--              <span style="float: right">-->
            <!--                <router-link class="primary" to="">-->
            <!--                无法验证?-->
            <!--              </router-link>-->
            <!--              <router-link class="primary" to="">-->
            <!--                忘记密码?-->
            <!--              </router-link>-->
            <!--              </span>-->
            <!--            </div>-->
            <!--            <el-form-item style="margin-top: 20px">-->
            <!--              <el-button style="width: 45%;color: white" type="primary">登录</el-button>-->
            <!--              <el-button style="width: 45%;float: right"> 注册</el-button>-->
            <!--            </el-form-item>-->
            <el-form-item>
              <el-input>
                <el-button slot="append" placeholder="请输入短信验证码">
                  点击获取
                </el-button>
              </el-input>
            </el-form-item>
            <el-form-item>
              <div style="font-size: 10px">
                <el-checkbox v-model="checkBill">
                </el-checkbox>
                我已同意
                <router-link class="primary" to="">
                  《噼里啪啦弹幕网用户使用协议》
                </router-link>
                和
                <router-link class="primary" to="">
                  《噼里啪啦隐私政策》
                </router-link>
              </div>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" style="width: 100%;color: white" :disabled="!checkBill" @click="toRegister">注册
              </el-button>
            </el-form-item>
            <el-form-item>
              <router-link class="primary" to="/login" style="font-size: 10px;float: right">
                已有账号 ,直接登录>
              </router-link>
            </el-form-item>
          </el-form>
        </el-col>

      </el-col>
    </el-row>


  </div>
</template>

<script>
    import AccountHeader from "@/views/account/AccountHeader";
    import AccountLoginOrRegisterHeaderImage from "@/views/account/AccountLoginOrRegisterHeaderImage";
    import {register} from "@/api/UserApi";
    import Message from "element-ui/packages/message/src/main";

    export default {
        components: {
            AccountLoginOrRegisterHeaderImage,
            AccountHeader
        },
        name: "AccountRegister",
        data: () => ({
            list: [
                {label: '中国', value: '+86'},
                {label: '美国', value: '??'},
                {label: '??', value: '???'},
            ],
            val: '',
            checkBill: false,
            form: {
                name: '',
                password: '',
                phone: ''
            }
        }),
        methods: {
            toRegister() {
                register(this.form).then(resp => {
                    let {msg} = resp.data
                    console.log(msg)
                    // if (msg) {
                    // this.$message(msg)
                    this.$message.success({
                        message: 'asd'
                    })
                    // Message(msg)
                    // }
                })
            }
        }
    }
</script>

<style scoped>

</style>
