<template>
  <div>
    <!--    asdads-->
  </div>
</template>

<script>
    import AccountHeader from "../account/AccountHeader";

    export default {
        name: "AccountHome",
        components: {
            AccountHeader
        },
        data() {
            return {
                list: [
                    {
                        name: '主页',
                    },
                    {
                        name: '动态',
                    },
                    {
                        name: '投稿',
                    },
                    {
                        name: '频道',
                    },
                    {
                        name: '收藏',
                    },
                    {
                        name: '订阅',
                    },
                    {
                        name: '设置',
                    },
                ],
                activeIndex: '主页'
            }
        }
    }
</script>

<style scoped>

</style>
