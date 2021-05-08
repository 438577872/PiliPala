<template>
  <div>
    <!--    <Account-->
    <AccountHeader></AccountHeader>
    <AccountBody></AccountBody>
    <!--    <div id="foot" ref="foot"></div>-->
    <AccountFoot></AccountFoot>
  </div>
</template>

<script>
    import Fanjv from "../../components/icons/Fanjv";
    import AccountHeader from "./AccountHeader";
    import AccountBody from "./AccountBody";
    import AccountFoot from "./AccountFoot";

    export default {
        name: "Layout",
        components: {AccountFoot, AccountBody, AccountHeader, Fanjv},
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

                    list3: [
                        {
                            name: '首页',
                            number: 2455
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
                }
            }
        },
        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            },
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
  #head {

    /*background: #000;*/

  }

  #body {
    min-height: 800px;
    /*background-image: url("http://img.daimg.com/uploads/allimg/210405/3-210405221112.jpg");*/
    /*background: rgb();*/
    /*opacity: 0.5;*/
  }

  #foot {
    min-height: 400px;
    background: rgb(246, 249, 250);
  }
</style>
