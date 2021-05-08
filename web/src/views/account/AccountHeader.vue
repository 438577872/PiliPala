<template>
  <el-card body-style="padding:0">
    <el-row style="padding-left: 0px;padding-top: 10px;line-height: 36px;font-size: 14px">
      <el-col :span="8" :offset="0">
        <el-row type="flex">
          <div style="margin-left: 50px">
            <el-image src="/favicon.ico"
                      style="height: 20px;width: 20px;position: relative;top: 5px"></el-image>
            <router-link to="/">
            <span style="color: black;margin-left: 10px">主站</span>
            </router-link>
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
                       height: 36px;border: 1px solid rgba(0,0,0,0);">
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
    import {staticAvatar} from "@/config";
    import {mapGetters} from "vuex";
    import AccountLoginDialog from "@/views/account/AccountLoginDialog";
    import AccountLogoutDialog from "@/views/account/AccountLogoutDialog";
    import PublicAvatar from "@/views/Public/PublicAvatar";

    export default {
        name: "PublicHeaderOrdinary",
        components: {PublicAvatar, AccountLogoutDialog, AccountLoginDialog, AccountHeader},

        data() {
            return {
                list: [
                    {
                        name: '助战'
                    },
                    {
                        name: '助战'
                    },
                    {
                        name: '助战'
                    },
                    {
                        name: '助战'
                    },
                    {
                        name: '助战'
                    },
                    {
                        name: '助战'
                    }, {
                        name: '助战'
                    }, {
                        name: '助战'
                    },
                ],
                list2: [
                    {
                        name: '创作中心'
                    }, {
                        name: '创作中心'
                    }, {
                        name: '创作中心'
                    }, {
                        name: '创作中心'
                    }, {
                        name: '创作中心'
                    },
                ],
                menu: {
                    list: [
                        {
                            'name': '番剧'
                        },
                        {
                            'name': '游戏中心'
                        },
                        {
                            'name': '直播'
                        },
                        {
                            'name': '会员购'
                        },
                        {
                            'name': '漫画'
                        },
                        {
                            'name': '赛事'
                        }
                    ],

                    list2: [
                        {
                            name: '大会员'
                        },
                        {
                            name: '消息'
                        },
                        {
                            name: '动态'
                        },
                        {
                            name: '收藏'
                        },
                        {
                            name: '历史'
                        },
                        {
                            name: '创作中心'
                        },
                    ],
                    list4: [
                        {
                            name: '动画',
                            number: 12
                        },
                        {
                            name: '番剧',
                            number: 124
                        },
                        {
                            name: '国际',
                            number: 125
                        },
                        {
                            name: '英语',
                            number: 365
                        },
                        {
                            name: '舞蹈',
                            number: 13
                        },
                        {
                            name: '游戏',
                            number: 15
                        },
                        {
                            name: '知识',
                            number: 136
                        },
                        {
                            name: '数码',
                            number: 16
                        },
                        {
                            name: '生活',
                            number: 126
                        },
                    ],
                    list5: [
                        {
                            name: '美食'
                        },
                        {
                            name: '动物圈'
                        },
                        {
                            name: '国际'
                        },
                        {
                            name: '英语'
                        },
                        {
                            name: '舞蹈'
                        },
                        {
                            name: '游戏'
                        },
                        {
                            name: '知识'
                        }
                    ]
                },
                staticAvatar
            }
        }
    }
</script>

<style scoped>

</style>