<script lang="ts">
    import { Grid, Text } from '@threlte/extras'
  
    export let text: string
    export let fontSize: number
  
  </script>
  
  
  <Text
    {text}
    color="white"
    {fontSize}
    anchorX="50%"
    anchorY="100%"
  />
  
  <Grid sectionColor="#FF3E00" />
  