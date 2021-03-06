from fortran_format import *
from for2py_arrays import *

def main():
    A = Array([(1,5),(1,5)])

    for i in range(1,5+1):
        for j in range(1,5+1):
            A.set((i,j), 11*(i+j))          # A(i,j) = 11*(i+j)


    fmt_obj_10 = Format(['5(I5)'])
    fmt_obj_11 = Format(['""'])

    for i in range(1,5+1):
        sys.stdout.write(fmt_obj_10.write_line([A.get((i,1)), A.get((i,2)), \
                                                A.get((i,3)), A.get((i,4)), \
                                                A.get((i,5))]))
    sys.stdout.write(fmt_obj_11.write_line([]))

    dim1 = implied_loop_expr((lambda x: x), 2, 4, 1)
    dim2 = implied_loop_expr((lambda x: x), 2, 4, 1)
    A_subs = idx2subs([values(dim1), values(dim2)])    # A( 2:4, 2:4)
    A.set_elems(A_subs, 0)

    for i in range(1,5+1):
        sys.stdout.write(fmt_obj_10.write_line([A.get((i,1)), A.get((i,2)), \
                                                A.get((i,3)), A.get((i,4)), \
                                                A.get((i,5))]))



main()
