<script lang="ts">
    import { T, useFrame } from '@threlte/core'
    import { MeshLineGeometry, Text } from '@threlte/extras'
    import {LineCurve3} from 'three';
    import type {  Vector3 } from 'three';
    
    export let centre: Vector3;
    export let type: string;
    export let name: string;
    export let color : string;

    let rotation = 0
    useFrame(() => {
        rotation += 0.001
    })

</script>
    
<T.Mesh position.x={centre.x -5} position.y={centre.y -1} position.z={centre.z -5}>
    <T.SphereGeometry args={[5, 500]}/>
    <T.MeshStandardMaterial color={color} />
    <!--<T.MeshPhongMaterial color={'red'} specular='yellow' shininess={100} Intersection={true}/>-->
</T.Mesh>

<T.Mesh position.x={centre.x -3} position.y={centre.y} position.z={centre.z -3}>
    <T.SphereGeometry args={[5, 500]}/>
    <T.MeshStandardMaterial color={color} />
</T.Mesh>

<T.Mesh position.x={centre.x} position.y={centre.y} position.z={centre.z} >
    <T.SphereGeometry args={[7, 500]} />
    <T.MeshStandardMaterial color={color} bumpScale={2}/>
</T.Mesh>


<T.Mesh position.x={centre.x +3} position.y={centre.y -1} position.z={centre.z +3}>
    <T.SphereGeometry args={[5, 500]}/>
    <T.MeshStandardMaterial color={color} />
</T.Mesh>

<T.Mesh position.x={centre.x -4} position.y={centre.y +2} position.z={centre.z -4}>
    <T.SphereGeometry args={[5, 500]}/>
    <T.MeshStandardMaterial color={color} />
</T.Mesh>

<T.Mesh position.x={centre.x -4} position.y={centre.y +3} position.z={centre.z -4}>
    <T.SphereGeometry args={[4, 500]}/>
    <T.MeshStandardMaterial color={color} />
</T.Mesh>

<T.Mesh position.x={centre.x} position.y={centre.y +4} position.z={centre.z}>
    <T.SphereGeometry args={[5, 500]}/>
    <T.MeshStandardMaterial color={color} />
</T.Mesh>


<Text
    position.z={centre.z -5}
    position.x={centre.x -5}
    position.y={centre.y-10}
    text={name + '/' + type}
    fontSize={4.8}/>


