<script lang="ts">
    import { T, useFrame } from '@threlte/core'
    import { MeshLineGeometry, Text } from '@threlte/extras'
    import {LineCurve3} from 'three';
    import type {  Vector3 } from 'three';
    
    export let position: Vector3;
    export let name: string = '';
    export let color : string;

    let rotation = 0
    useFrame(() => {
        rotation += 0.001
    })

</script>
    


<T.Mesh position.x={position.x} position.y={position.y} position.z={position.z} rotation.x={-Math.PI/2} >
    <T.CircleGeometry args={[7, 500]} />
    <T.MeshStandardMaterial color={color} transparent={false} opacity={0.8}/>
</T.Mesh>

<Text
    position.z={position.z -5}
    position.x={position.x -5}
    position.y={position.y-10}
    text={name}
    fontSize={4.8}/>


