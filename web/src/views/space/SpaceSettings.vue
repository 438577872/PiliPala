<template>
  <el-card>
    <SpaceTitleFont title="我的设置"></SpaceTitleFont>
<!--    <el-divider></el-divider>-->
    <br>
    <table>
      <tr  v-for="item in privacies">
        <td style="width: 200px;height: 30px;font-size: 14px">{{item.name }}</td>
        <td>
          <el-switch v-model="item.isOpen"></el-switch>
          <span class="font-dark-gray" style="margin-left: 20px;font-size: 14px" v-text="item.isOpen?'公开':'隐藏'"></span>
        </td>
      </tr>
    </table>
    <el-divider></el-divider>



  </el-card>

</template>

<script>
    import SpaceTitleFont from "@/views/space/components/SpaceTitleFont";
    export default {
        name: "SpaceSettings",
        components: {SpaceTitleFont},
        data() {
            return {
                privacies: [
                    {
                        'name': '我的收藏',
                        'isOpen': false
                    }, {
                        'name': '追番追剧',
                        'isOpen': false
                    }, {
                        'name': '订阅标签',
                        'isOpen': false
                    }, {
                        'name': '最近投币的视频',
                        'isOpen': false
                    }, {
                        'name': '个人资料',
                        'isOpen': false
                    }, {
                        'name': '最近玩过的游戏',
                        'isOpen': false
                    }, {
                        'name': '我的关注列表',
                        'isOpen': true
                    },
                ]
            }
        }
    }
</script>

<style scoped>

</style>
