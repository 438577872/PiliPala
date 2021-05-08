<template>
  <div class="header-background"
       @mousemove="over" @mouseleave="leave" @mouseenter="enter">
    <video loop src="/static/header.mp4"
           autoplay
           class="header-movie"
           :style="{transform: `scale(1) translate(${X}px, 0px) rotate(0deg)`}"
           ref="animate-video"/>
    <el-row style="padding-left: 0px;padding-top: 10px;line-height: 36px;font-size: 14px">
      <el-col :span="8" :offset="0">
        <el-row type="flex">
          <div style="margin-left: 50px">
            <el-image src="https://www.bilibili.com/favicon.ico?v=1"
                      style="height: 20px;width: 20px;position: relative;top: 5px"></el-image>
            <router-link to="/">
              <span style="color: white;margin-left: 10px">主站</span>
            </router-link>
          </div>
          <div style="margin-left: 20px" v-for="item in menu.list">
            <span style="color: white">{{item.name}}</span>
          </div>
        </el-row>
        <router-link to="/">
          <el-image class="bilibili-summer" src="/static/bilibili_summer.png"/>
        </router-link>
      </el-col>
      <el-col :span="6">
        <el-input>
          <el-button slot="append">
            <IconSearch/>
          </el-button>
        </el-input>
      </el-col>
      <el-col :span="10">
        <el-row type="flex" style="float: right">
          <div style="margin-right: 20px">
            <PublicAvatar/>
          </div>
          <div v-for="item in menu.list2" style="margin-right: 20px">
            <span style="color: white" v-text="item.name"/>
          </div>
          <div>
            <el-button size="medium"
                       v-text="'投稿'"
                       class="contribution-button"/>
          </div>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    import AccountHeader from "../account/AccountHeader";
    import {staticAvatar} from "@/config";
    import {mapGetters} from "vuex";
    import AccountLoginDialog from "@/views/account/AccountLoginDialog";
    import AccountLogoutDialog from "@/views/account/AccountLogoutDialog";
    import PublicAvatar from "@/views/Public/PublicAvatar";
    import {menu, list, list2} from "@/views/Public/nav_list";
    import IconSearch from "@/components/icons/IconSearch";

    export default {
        name: "PublicHeader",
        components: {IconSearch, PublicAvatar, AccountLogoutDialog, AccountLoginDialog, AccountHeader},

        data() {
            return {
                list,
                list2,
                menu,
                staticAvatar,
                X: -70,
                baseX: 0,

            }
        },
        methods: {
            over(e) {
                this.X = -70 - (e.clientX - this.baseX) * 0.02
            },
            leave(e) {
                this.$refs['animate-video'].animate([
                    {transform: `translateX(${this.X}px)`},
                    {transform: 'translateX(-70px)'}
                ], {
                    duration: 300,
                })
                this.baseX = -70
                this.X = -70
            },
            enter(e) {
                this.baseX = e.clientX
            }
        }
    }
</script>

<style scoped>
  /* 动画代码 */
  @keyframes header-movie {
    /*from {background-color: red;}*/
    /*to {background-color: yellow;}*/
  }

  /* 向此元素应用动画效果 */
  .header-movie {
    position: absolute;
    height: 180px;
    width: 2110px;
    top: 0;
    left: 0;
    object-fit: cover;
    opacity: 1;
    animation-name: header-movie;
    animation-duration: 4s;
    transform: matrix();
  }

  .contribution-button {
    margin-right: 50px;
    background: rgb(251, 114, 153);
    color: white;
    width: 100px;
    height: 36px;
    border: 0px solid black;
  }

  .header-background {
    background-image: url('/static/header.mp4');
    height: 180px;
    width: 100%;
    overflow: hidden !important;
    position: relative;
  }

  .bilibili-summer {
    margin-left: 200px;
    margin-top: 20px;
    position: absolute;
    width: 200px
  }

</style>