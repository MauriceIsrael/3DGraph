<script lang="ts">
    import { T } from '@threlte/core'
    import { useTexture } from '@threlte/extras'
    import type { Vector3 } from 'three';
  
    const map = useTexture('AVATAR.png')
    const etage = 80;
    export let position: Vector3;
  </script>
  
  {#await map then value}
    <T.Mesh position.x={position.x} position.y={2*etage} position.z={position.z} scale.x=5 scale.y=5 scale.z=5>
      <T.BoxGeometry />
      <T.MeshBasicMaterial map={value} />
    </T.Mesh>
  {/await}
  