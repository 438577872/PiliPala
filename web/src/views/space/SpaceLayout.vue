<template>
  <div>

    <AccountHeader></AccountHeader>
    <el-row>
      <el-col :span="16" :offset="4">
        <el-card body-style="padding:0">
          <div
                  style="background: url('/static/img/cb1c3ef50e22b6096fde67febe863494caefebad.png@2560w_400h_100q_1o.webp');
                    height: 200px;;position: relative;">
            <div style="position: absolute;;width: 100%;height: 100%;
                  background-image: linear-gradient(rgba(255,255,255,0),rgba(0,0,0,0.3));">
            </div>
            <div style="position: absolute;top: 120px;left: 30px;width: 100%">
              <el-row>
                <el-col :span="1">
                  <el-avatar
                          :src="staticAvatar+avatar"
                          style="width: 65px;height: 65px;border: 1px solid white">
                  </el-avatar>
                </el-col>
                <el-col :offset="1" :span="20">
                  <b class="font-white" style="font-size: 18px">
                    {{name}}
                  </b>
                </el-col>
              </el-row>
            </div>
          </div>
<!--          (item.path || item.path=='')?item.path:item.redirect-->
          <el-menu :default-active="activeIndex" mode="horizontal" router>
            <el-menu-item style="margin-left:10px" :key="item.name" :index="(item.meta && item.meta.url)?item.meta.url:item.path"
                          v-for="item in list">
              <span slot="title">{{item.name}}</span>
            </el-menu-item>

          </el-menu>
        </el-card>
        <router-view style="margin-top: 20px"></router-view>
      </el-col>
    </el-row>

  </div>
</template>

<script>
    import AccountHeader from "../account/AccountHeader";
    import {spaceList} from '@/router/index.js'
    import {mapGetters} from "vuex";
    import {staticAvatar} from "@/config";

    export default {
        name: "SpaceLayout",
        components: {AccountHeader},
        computed: {
            ...mapGetters([
                'avatar', 'name'
            ])
        },
        data() {
            return {
                list: spaceList,
                activeIndex: 'home',
                background: '',
                staticAvatar,
                title: ''
            }
        },
        methods: {
            to(url, redirect) {
                if (redirect) {
                    this.$router.push(redirect)
                } else {
                    this.$router.push(url)
                }
            },
        },
        mounted() {
            let paths = this.$route.path.split('/')
            this.activeIndex = paths[paths.length - 1]
            this.background = document.getElementsByTagName('body')[0].style.background
            document.getElementsByTagName('body')[0].style.background = 'rgb(244,245,247)'
            // let title
            this.title = document.title
            document.title = this.name + '的空间'

        },
        destroyed() {
            document.getElementsByTagName('body')[0].style.background = this.background
            document.title =this.name

        }
    }
</script>

<style scoped>

</style>
