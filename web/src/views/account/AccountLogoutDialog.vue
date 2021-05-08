<template>
  <div style=";z-index: -1;text-align: center">
<!--    <div>-->
<!--      <el-button type="primary" style="width: 100%;color: white">立即登录</el-button>-->
<!--    </div>-->
    <div style="margin-top: 10px">

      <el-button @click="logOut">
        退出登录
      </el-button>
    </div>
  </div>
</template>

<script>
    export default {
        name: "AccountLogoutDialog",
        data(){
            return{}
        },
        methods:{
            logOut(){
                this.$store.dispatch('user/logout')
            }
        }
    }
</script>

<style scoped>

</style>
