<script lang="ts">
    import { T } from '@threlte/core'
    import { MeshLineGeometry, MeshLineMaterial } from '@threlte/extras'
    import {LineCurve3} from 'three';
    import type { Vector3 } from 'three';
    
    export let source: Vector3;
    export let destination: Vector3;
    export let color : string;
    
    // convert curve to an array of 100 points
    // const points = [source, destination]
    const curve= new LineCurve3(source, destination)
    let taper = curve.getPoints(100)
    let dashArray = 0
    let dashRatio = 1

    //gestion des liens verticaux
    if ((source.x == destination.x) && (source.z == destination.z)) {
        dashArray = 0.1
        dashRatio = 0.5
        color = 'Pink'
    }
        
</script>
   
  <T.Mesh position.x={source.x} position.y={source.y} position.z={source.z}>
    <T.SphereGeometry args={[1, 100]}/>
    <T.MeshStandardMaterial color={color} />
  </T.Mesh>
  
  <T.Mesh position.x={destination.x} position.y={destination.y} position.z={destination.z}>
    <T.SphereGeometry args={[1, 100]}/>
    <T.MeshStandardMaterial color={color} />
  </T.Mesh>
  
  <T.Mesh >
    <MeshLineGeometry points={taper} shape="taper"/>
    <MeshLineMaterial color={color} dashArray={dashArray} dashRatio={dashRatio} dashOffset={0} transparent={true} opacity={1} width={0.3}/>
  </T.Mesh>
  
  