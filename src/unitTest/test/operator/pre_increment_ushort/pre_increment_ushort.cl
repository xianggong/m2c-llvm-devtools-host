// Auto generated kernel

__kernel void pre_increment_ushort(__global ushort *src_0, __global ushort* dst)
{
	int gid = get_global_id(0);
	dst[gid] = ++ src_0[gid] ;
}
