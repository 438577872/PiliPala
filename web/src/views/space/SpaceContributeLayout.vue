<template>
  <el-card body-style="padding:0">
    <el-row>
      <el-col :span="4" style="min-height: 500px;border-right: 1px solid rgb(221,221,221)">
        <el-menu
                active-text-color="#fff"
                text-color="#000000"
                router
        >
          <el-menu-item @click="active=item.name" v-for="item in SpaceContributeList" :key="item.path"
                        :index="item.path"
                        style="padding-left: 0;padding-right: 0">
            <div :style="{
                background: active===item.name?'rgb(0,161,214)':'',
                color: active===item.name?'white':'',
            }"
                 style="padding-left: 20px;padding-right: 20px">
              <span>
              {{item.name}}
            </span>
              <span style="float: right">
              {{item.val}}
            </span>
            </div>
          </el-menu-item>

        </el-menu>
      </el-col>
      <el-col :span="20" style="padding: 0px">

        <el-row>
          <router-view></router-view>
        </el-row>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
    import {SpaceContributeList} from '@/router/index'

    export default {
        name: "SpaceContributeLayout",
        data() {
            return {
                list: [
                    {
                        name: '视频',
                        val: 0
                    },
                    {
                        name: '音频',
                        val: 0
                    }, {
                        name: '专栏',
                        val: 0
                    }, {
                        name: '相册',
                        val: 0
                    }
                ],
                SpaceContributeList,
                active: '视频'
            }
        }
    }
</script>

<style scoped lang="scss">
  .active {
    background: #000;
  }
</style>
