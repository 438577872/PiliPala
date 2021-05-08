<template>
  <el-collapse v-model="activeName" accordion>
    <el-collapse-item title="选集" name="2">
      <el-table :data="nos">
        <el-table-column prop="no" label="P">
          <template slot-scope="{row}">
            <el-link @click="changeVideo(row.no)">
              {{row.no}}
            </el-link>
          </template>
        </el-table-column>
        <el-table-column prop="createAt" label="标题"/>
      </el-table>
    </el-collapse-item>
    <el-collapse-item title="弹幕列表" name="1">
      <el-table :data="barrage" height="500px">
        <el-table-column label="时间" width="100">
          <template slot-scope="{row}">
            {{row.time}}秒
          </template>
        </el-table-column>
        <el-table-column prop="msg" label="弹幕内容">
          <template slot-scope="{row}">
            {{row.msg.length>12?row.msg.substr(0,12)+'...':row.msg}}
          </template>
        </el-table-column>
        <el-table-column prop="createAt" label="发送时间">
          <template slot-scope="{row}">
            <span style="font-size: 10px">{{row.createAt}}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-collapse-item>

  </el-collapse>
</template>

<script>
    import {getVideoUrlBySeriesIdAndNo} from "@/api/VideoApi";

    export default {
        name: "VideoRightComponent",
        data() {
            return{
                activeName:'2',


            }
        },
        methods:{
            changeVideo(no) {
                this.$emit('changeVideo',no)
            }
        },
        props:[
            'barrage',
            'nos'
        ]
    }
</script>

<style scoped>

</style>
