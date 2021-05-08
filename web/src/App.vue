<template>
  <div style="width: 100%">
    <div align="left">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'App',
        components: {},
        data: () => ({}),
    };
</script>
<style lang="scss">
  @import "src/styles.scss";

  .primary {
    color: $--color-primary;
  }

  .font-gray {
    color: rgb(203, 208, 216)
  }

  .font-dark-gray {
    color: rgb(132, 117, 122)
  }

  .font-white {
    color: white;
  }

  a {
    &:hover {
      text-decoration: none;
    }

    &:active {
      text-decoration: none;
    }

    &:visited {
      text-decoration: none;
    }

    &:link {
      text-decoration: none;
    }
  }

</style>
<style>
  body, html {
    min-width: 1900px;
    max-width: 1920px;
    overflow-x: auto !important;
    padding: 0 !important;
    margin: 0 !important;
  }
</style>