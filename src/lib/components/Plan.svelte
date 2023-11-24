<script lang="ts">
    import { T } from '@threlte/core'
    import { Text } from '@threlte/extras'

    export let plan = 0;
    export let color : string = 'cyan';
    export let name = ''

    const etage = plan * 80;
</script>

<!-- Disque bleu cyan-->
<T.Mesh position.y={etage} rotation.x={-Math.PI/2} receiveShadow>
    <T.CircleGeometry args={[200, 100]} />
    <T.MeshStandardMaterial color={color} transparent={true} opacity={0.3} />

    <Text
        text={name}
        position.y ={-110}
        fontSize={4.8}/>
</T.Mesh>