<script lang="ts">
    import { T } from '@threlte/core'
    import { MeshLineGeometry, MeshLineMaterial } from '@threlte/extras'
    import {CatmullRomCurve3, Vector3 } from 'three';
   
    export let controlPoints: Vector3[]
    export let color : string;
    
    // convert curve to an array of 100 points
    // const points = [source, destination]
    const curve= new CatmullRomCurve3(controlPoints, false, 'catmullrom', 0.5)
    let taper = curve.getPoints(100)

        
</script>

  
  <T.Mesh >
    <MeshLineGeometry points={taper} shape="taper"/>
    <MeshLineMaterial color={color} transparent={true} opacity={1} width={1.5}/>
  </T.Mesh>
  
  