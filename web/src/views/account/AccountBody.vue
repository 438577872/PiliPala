<template>
  <div id="body" ref="body" style="padding-top: 30px">
    <el-card body-style="padding:0" style="width: 60%;margin-left: auto;margin-right: auto">
      <el-row style="height: 50px;">
        <el-col :span="3" style="border-right: 1px solid rgb(221,221,221);height: 100%;padding-top: 15px">
          <span style="margin-left: 30px">个人中心</span>
        </el-col>
        <el-col :span="21"
                style="border-bottom: 1px solid rgb(221,221,221);height: 100%;padding-top: 15px;padding-left: 20px">
          大会员
        </el-col>
      </el-row>
      <div>
        <el-row>
          <el-col :span="3">
            <el-menu
                default-active="2"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
                style="border: 1px solid rgb(221,221,221);"
                text-color="#fff"
                active-text-color="black">
              <el-menu-item v-for="item in menu.list3" :key="item.to" index="2">
                <a slot="title" :href="item.to">{{item.name}}</a>
              </el-menu-item>
            </el-menu>
          </el-col>
          <el-col :span="21" style="padding: 20px">

           <router-view>

           </router-view>
          </el-col>
        </el-row>
      </div>
    </el-card>

  </div>
</template>

<script>
    export default {
        name: "AccountBody",
        data() {
            return {
                style: {
                    head: {
                        height: '30px',
                        background: '#000',

                    }
                },
                activeIndex: '1',
                activeIndex2: '1',
                menu: {

                    list3: [
                        {
                            name: '首页',
                            'to':'home'
                        },
                        {
                            name: '大会员',
                            number: 2455
                        },
                        {
                            name: '会员积分',
                            number: 2455
                        },
                        {
                            name: '我的信息',
                            number: 2455
                        },
                        {
                            name: '我的头像',
                            number: 2455
                        },
                        {
                            name: '我的勋章',
                            number: 2455
                        },
                        {
                            name: '账号安全',
                            number: 2455
                        },
                        {
                            name: '黑名单管理',
                            number: 2455
                        },
                        {
                            name: '我的硬币',
                            number: 2455
                        },
                        {
                            name: '我的记录',
                            number: 2455
                        },
                        {
                            name: '实名认证',
                            number: 2455
                        },
                        {
                            name: '邀请注册'
                        },
                    ],

                }
            }
        },
        methods: {
            // handleSelect(key, keyPath) {
            //     console.log(key, keyPath);
            // },
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            }
        }
    }
</script>

<style scoped>

</style>
