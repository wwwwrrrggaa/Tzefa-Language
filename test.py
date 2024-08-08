from createdpython import * 
line(1); addvar( "INT" , 'INTEGERONE' , 96 ); endline() ;
line(2); addvar( "INT" , 'INTEGERTWO' , 144 ); endline() ;
line(3); addvar( "INT" , 'TEMPTWO' , 0 ); endline() ;
line(4); addvar( "INT" , 'ZERO' , 0 ); endline() ;
line(5); addvar( "LIST" , 'GCDLIST' , getvar( 'INT' , 'INTEGERONE' ).read() ); endline() ;
line(6); addcond( 'GCDCOMPARE' , 'BIGGER' ); endline() ;
line(7); getcond( 'GCDCOMPARE' ).changeleft(getvar( "INT" , 'INTEGERTWO' )); endline() ;
line(8); getcond( 'GCDCOMPARE' ).changeright(getvar( "INT" , 'ZERO' )); endline() ;
def GCD():
    line(10); mod( 'INTEGERONE' , 'INTEGERTWO' ); endline()
    line(11); assignint( 'INTEGERONE' , 'INTEGERTWO' ); endline()
    line(12); assignint( 'INTEGERTWO' , 'TEMPORARY' ); endline()
    if( line(13) and getvar('BOOLEAN','LOOPBOOL').read() and endline() ):
