module.exports = {
  settings: {
    "vetur.useWorkspaceDependencies": true,
    "vetur.experimental.templateInterpolationService": true
  },
  projects: [
    {
      root: './docs',
      globalComponents: [
        './src/components/**/*.vue'
      ]
    }
  ]
}