<template>
  <button class="ui-tab-button" :class="[{'is-active': tab.isActive}]">
    <slot />
  </button>
</template>

<script>
export default {
  name: "UiTabButton",
  props: {
    tab: {
      type: Object,
      required: true
    }
  }
};
</script>

<style lang="scss">
</style>