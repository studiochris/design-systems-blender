<template>
  <keep-alive>
    <div class="ui-tab ui-tab-content" v-if="isActive"><slot /></div>
  </keep-alive>
</template>

<script>
export default {
  name: "UiTab",
  props: {
    name: {
      type: String,
      default: "Tab"
    },
    isActive: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      isUiTab: true
    };
  }
};
</script>

<style>
.ui-tab {
  border: 1px solid red;
}
</style>