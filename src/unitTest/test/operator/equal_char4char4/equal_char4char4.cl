// Auto generated kernel

__kernel void equal_char4char4(__global char4 *src_0, __global char4 *src_1, __global int4* dst)
{
	int gid = get_global_id(0);
	dst[gid] = (int4)( src_0[gid] == src_1[gid]);
}
