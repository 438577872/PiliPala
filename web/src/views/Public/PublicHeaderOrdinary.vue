<template>
  <el-card body-style="padding:0">
    <el-row style="padding-left: 0px;padding-top: 10px;line-height: 36px;font-size: 14px">
      <el-col :span="8" :offset="0">
        <el-row type="flex">
          <div style="margin-left: 50px">
            <el-image src="https://www.bilibili.com/favicon.ico?v=1"
                      style="height: 20px;width: 20px;position: relative;top: 5px"></el-image>
            <span style="color: black;margin-left: 10px">主站</span>
          </div>
          <div style="margin-left: 20px" v-for="item in menu.list">
            <span style="color: black ">{{item.name}}</span>
          </div>
        </el-row>
      </el-col>
      <el-col :span="6">
        <el-input>
          <el-button slot="append"></el-button>
        </el-input>
      </el-col>
      <el-col :span="10">
        <el-row type="flex" style="float: right">
          <div style="margin-right: 20px">
            <PublicAvatar></PublicAvatar>
          </div>
          <div v-for="item in menu.list2" style="margin-right: 20px">
            <span style="color: black">{{item.name}}</span>
          </div>
          <div>
            <el-button size="medium"
                       style="margin-right: 50px;
                       background: rgb(251,114,153);
                       color: white;width: 100px;
                       height: 36px;border: 1px solid black;">
              投稿
            </el-button>
          </div>
        </el-row>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
    import AccountHeader from "../account/AccountHeader";
    import AccountLoginDialog from "@/views/account/AccountLoginDialog";
    import AccountLogoutDialog from "@/views/account/AccountLogoutDialog";
    import PublicAvatar from "@/views/Public/PublicAvatar";
    import {list, list2, menu} from "@/views/Public/nav_list";
    import {staticAvatar} from "@/config";
    import {mapGetters} from "vuex";

    export default {
        name: "PublicHeaderOrdinary",
        components: {PublicAvatar, AccountLogoutDialog, AccountLoginDialog, AccountHeader},

        data() {
            return {
                list,
                menu,
                list2,
                staticAvatar
            }
        }
    }
</script>

<style scoped>

</style>