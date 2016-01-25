// Auto generated kernel

__kernel void clz_uint16(__global uint16 *src_0, __global uint16* dst)
{
	int gid = get_global_id(0);
	dst[gid] = clz(src_0[gid]);
}
