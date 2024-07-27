from createdpython import * 
line(1); addvar( "INT" , 'INTEGERONE' , 96 ); endline() ;
line(2); addvar( "INT" , 'INTEGERTWO' , 144 ); endline() ;
line(3); addvar( "INT" , 'TEMPTWO' , 0 ); endline() ;
line(4); addvar( "INT" , 'ZERO' , 0 ); endline() ;
line(5); addcond( 'GCDCOMPARE' , 'BIGGER' ); endline() ;
line(6); getcond( 'GCDCOMPARE' ).changeleft(getvar( "INT" , 'INTEGERTWO' )); endline() ;
line(7); getcond( 'GCDCOMPARE' ).changeright(getvar( "INT" , 'ZERO' )); endline() ;
while( line(8) and getcond( 'GCDCOMPARE' ).giveresult() and endline() ):
    line(9); mod( 'INTEGERONE' , 'INTEGERTWO' ); endline()
    line(10); assignint( 'INTEGERONE' , 'INTEGERTWO' ); endline()
    line(11); assignint( 'INTEGERTWO' , 'TEMPORARY' ); endline()
printvars()