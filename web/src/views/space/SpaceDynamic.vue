<template>
  <div>
    <el-row :gutter="20">
      <el-col  :span="16" style="text-align: center">
        <el-card :body-style="{
            'padding-top':'50px',
            'padding-bottom':'50px',
        }">
          <el-image src="https://s1.hdslb.com/bfs/seed/bplus-common/dynamic-assets/empty.png">

          </el-image>
          <br>
          哦呀，TA还没有动态呢~
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          仅自己可见
          <br>
          280535116 02-18
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    export default {
        name: "SpaceDynamic"
    }
</script>

<style scoped>

</style>
