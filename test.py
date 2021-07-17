import unittest
import functions

class test_function_F(unittest.TestCase):

    def test_F_Neg(self):
        with self.assertRaises(AssertionError):
            functions.F(-1)

    def test_F_0(self):
        self.assertEqual(functions.F(0), [0])

    def test_F_1(self):
        self.assertEqual(functions.F(1), [0,1])

    def test_F_15(self):
        self.assertEqual(functions.F(15), [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610])
    
    def test_F_4999(self):
        self.assertEqual(functions.F(4999)[4999], 2397334346100631452333336800023778743396400988090212332865227234032387117767626167465060795065595580850691237390963845987165478074085124644348902530685083246709423858342692329718110162972268152200857232686119638781547238020078362945470777668711057069618425746387920931255084621360135655698456629322111614827324455767748623844363426260372374195153577101298837831208580530677289982029527164306876024342838547454228388796380077029917639469963653048076473269452943584037848773158456736367057460079075603072996653089318046279296240100777360367200040226807430924334616931577257195085793060133817911514540227011756335999604550121968663793604830945238116686325506344893928776515696088851468818023735825546502317562957459506612704850760351077006532507519813600498603205937022956740021970327599548184626715032015801445754074519753924901317605013561516613650173445818028242577356369143977719495739428130191089993769093308407443558168431535751910046557480949313497996285124526992631353143367314930548703966553707195171094152730704138121243470432644848607501)

    def test_F_with_cache_15(self):
        functions.F_with_cache(5,1,100)
        self.assertEqual(functions.F_with_cache(15,1,100)[15], functions.fab_cache[15])
        functions.fab_cache=[]

    def test_F_with_cache_4999(self):
        self.assertEqual(functions.F_with_cache(4999,1,100000)[4999], '2397334346100631452333336800023778743396400988090212332865227234032387117767626167465060795065595580850691237390963845987165478074085124644348902530685083246709423858342692329718110162972268152200857232686119638781547238020078362945470777668711057069618425746387920931255084621360135655698456629322111614827324455767748623844363426260372374195153577101298837831208580530677289982029527164306876024342838547454228388796380077029917639469963653048076473269452943584037848773158456736367057460079075603072996653089318046279296240100777360367200040226807430924334616931577257195085793060133817911514540227011756335999604550121968663793604830945238116686325506344893928776515696088851468818023735825546502317562957459506612704850760351077006532507519813600498603205937022956740021970327599548184626715032015801445754074519753924901317605013561516613650173445818028242577356369143977719495739428130191089993769093308407443558168431535751910046557480949313497996285124526992631353143367314930548703966553707195171094152730704138121243470432644848607501')
        functions.fab_cache=[]

    def test_F_with_cache_index_error(self):
        functions.F_with_cache(50,1,100)
        with self.assertRaises(IndexError):
            functions.F_with_cache(5,1,100)[15]
        functions.fab_cache=[]

    def test_F_with_cache_empty_page(self):
        self.assertEqual(functions.F_with_cache(15,2,100), [])
        functions.fab_cache=[]

    def test_F_with_cache_pages(self):
        self.assertEqual(functions.F_with_cache(15,1,10), ['0','1','1','2','3','5','8','13','21','34'])
        self.assertEqual(functions.F_with_cache(15,2,10), ['55','89','144','233','377','610'])
        functions.fab_cache=[]
    
if __name__ == '__main__':
    unittest.main(verbosity=2)