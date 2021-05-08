<template>
  <el-row :gutter="10" style="margin-top: 20px">
    <slot name="icon"></slot>
    <label style="line-height: 60px;font-size: 20px">
      {{title}}
    </label>
    <br>
    <el-col :span="24">
      <el-col :span="4"  v-for="item in promotions" :key="item.to">
        <a :href="item.to" target="_blank">
          <el-image
              :src="item.pic">
          </el-image>
          <el-link :underline="false" style="font-size: 12px">
            {{item.title}}
          </el-link>
          <br>
          <el-link style="font-size: 10px" :underline="false">
            UP: {{item.up}}
          </el-link>
        </a>
      </el-col>
    </el-col>
    <el-col :span="4"></el-col>
  </el-row>
</template>

<script>
    import IconVoice from "@/components/icons/IconVoice";

    export default {
        name: "HomeOtherContents",
        components: {IconVoice},
        props: [
            'promotions',
            'title',
            // 'modules'
        ]
    }
</script>

<style scoped>

</style>
