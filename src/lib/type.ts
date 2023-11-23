import type { Vector3 } from 'three';
type Link = {
	source: Vector3;
    destination: Vector3;
    color : string;
}
type Flow = {
	name: string;
    controlPoint: Vector3[];
    }

export type Links = Array<Link | null>
export type Flows = Array<Flow | null>