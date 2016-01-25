// Auto generated kernel

__kernel void abs_diff_uchar16uchar16(__global uchar16 *src_0, __global uchar16 *src_1, __global uchar16* dst)
{
	int gid = get_global_id(0);
	dst[gid] = abs_diff(src_0[gid], src_1[gid]);
}
