// Auto generated kernel

__kernel void relational_less_than_or_equal_to_uint16uint16(__global uint16 *src_0, __global uint16 *src_1, __global int16* dst)
{
	int gid = get_global_id(0);
	dst[gid] = (int16)( src_0[gid] <= src_1[gid]);
}
