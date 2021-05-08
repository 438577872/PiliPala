<template>

  <el-row>
    <el-col style="padding: 20px">
      <el-row>
        <SpaceTitleFont title="我要投稿"></SpaceTitleFont>
      </el-row>
      <el-row>
        <div align="center" style="padding-top: 120px">
          <el-button type="primary" style="color: white;;" @click="showDialog">点击投稿</el-button>
          <el-dialog :visible.sync="uploadDialog" align="left">
            <template slot="title">
              上传
            </template>
            <SpaceUploadDialog ></SpaceUploadDialog>
          </el-dialog>
        </div>
      </el-row>
    </el-col>
  </el-row>

</template>

<script>
    import SpaceTitleFont from "@/views/space/components/SpaceTitleFont";
    import SpaceUploadDialog from "@/views/space/components/SpaceUploadDialog";

    export default {
        name: "SpaceUpload",
        components: {SpaceUploadDialog, SpaceTitleFont},
        data() {
            return {
                uploadDialog: false
            }
        },
        methods: {
            showDialog() {
                this.uploadDialog = true
            }
        }
    }
</script>

<style scoped lang="scss">
  .active {
    background: #000;
  }
</style>
