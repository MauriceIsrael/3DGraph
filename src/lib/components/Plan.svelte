<script lang="ts">
    import { T } from '@threlte/core'

    export let plan = 0;
    export let color : string = 'cyan';

    const etage = plan * 40;
</script>



<!-- Disque bleu cyan-->
<T.Mesh position.y={etage} rotation.x={-Math.PI/2} receiveShadow>
    <T.CircleGeometry args={[120, 100]}/>
    <T.MeshStandardMaterial color={color} transparent={true} opacity={0.5}/>
</T.Mesh>