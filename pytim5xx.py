import usb.core
import usb.util
import time
import unicodedata
import struct
import ctypes

demo = False

def demo_data(a):

    if a == 1:

        telegram = ['sRA', 'LMDscandata', '1', '1', '1078AAA', '0', '0', '3C23', '3C25', '426E6678', '426E7BBC', '0', '0', '1', '0', '0', '5DC', 'A2', '0', '2', 'DIST1', '3F800000', '00000000', 'FFF92230', 'D05', '32B', '0', '0', 'D12', 'D1C', 'D39', 'D2F', 'CF3', 'CBC', 'CC9', 'D15', '821', '87D', '0', 'F28', '0', 'F1C', 'ED2', '2', '2', '2', '2', '804', '7FB', '7EC', '7E0', '7E0', '7D9', '7DA', '7DA', '7DE', '7E2', '7E3', '7E4', '7DD', '7DF', '7E1', '7DF', '7E0', '7DF', '7E2', '7DD', '7DD', '7D6', '7D2', '7D2', '7D5', '7D2', '7DE', '7D9', '7D9', '2', 'A1C', 'A2E', 'A2B', 'A30', 'A3D', 'A38', 'A4B', 'A35', 'A1F', 'A1C', 'A3F', 'A5E', 'A4F', 'A0F', '999', '959', '954', '9C6', 'A54', 'A6D', 'A74', 'A7D', 'A7D', 'A6D', 'A67', 'A6B', 'A68', 'A60', '0', '0', '0', 'AD3', 'ADB', 'AEC', 'AF0', 'AFF', 'B04', 'B12', 'B17', 'B1C', 'B25', 'B2D', 'B3D', 'B47', 'B4B', 'B57', 'B63', 'B69', 'B76', 'B7B', 'B90', 'B8A', 'B95', 'BAA', 'BB2', 'BBB', 'BBE', 'BE3', 'BE3', '319', '271', '26C', '26B', '269', '26F', '26B', '26B', '26F', '269', '273', '273', '26D', '276', '27C', '27B', '286', '287', '294', '297', '29B', '29A', '299', '296', '28F', '294', '29B', '29B', '29E', '29E', '29C', '29C', '2A0', '2A1', '2A8', '2A0', '2A3', '2A0', '29C', '2A3', '2AF', '2B6', '2BA', '2B7', '2C3', '2CE', '2D1', '2D3', '2D5', '3B4', 'AB5', 'AC0', 'BD8', 'C4B', 'C48', 'C36', 'C32', 'C28', 'C23', 'C1A', 'C18', 'C12', 'C00', 'C02', 'BF4', 'BEF', 'BEA', 'BEA', 'BE1', 'BE7', 'CBA', 'CB4', 'C8F', 'C5F', 'C31', 'C0A', 'BE3', 'BBA', 'B92', 'B6C', 'B51', 'B3B', 'AF7', 'ACB', 'AC7', 'AC5', 'ACD', 'AAB', 'ABE', 'AA1', 'A95', 'AC9', 'B39', 'B51', 'B73', 'B7E', 'B9E', 'B98', 'BBA', 'BC8', 'BCD', '1280', '26B', '265', '25C', '267', '25B', '251', '24C', '257', '259', '255', '253', '256', '255', '250', '254', '250', '253', '252', '251', '249', '250', '24F', '252', '251', '252', '256', '259', '25B', '2', '5A9', '5A5', '59D', '597', '58C', '585', '581', '570', '56A', '573', '554', '500', '4FB', '4FD', '515', '51C', '51B', '524', '527', '535', '53B', '546', '551', '55D', '573', '577', '587', '597', '5A7', '5AA', '5C8', '5CA', '5DC', '5E6', '5F3', '610', '61D', '62A', '63E', '646', '643', '652', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '13F2', '0', '2', '2FC', '2FD', '2FB', '2FB', '2F6', '2F5', '2F5', '2F3', '2F3', '2EC', '2F8', '306', '305', '305', '306', '305', '301', '2F0', '2E1', '2E6', '2FE', '30C', '30F', '309', '305', '2F9', '2F2', '2E1', '2D2', '2D9', '2E5', '2EC', '2EC', '2E8', '2EC', '2E8', '2D4', '2C2', '2D8', '2D4', '2D9', '2E8', '2F9', '30F', '331', '343', '35D', '376', '3A1', '11E2', '1234', '1273', '1824', '1E53', '1757', '1151', '1157', '1152', '1136', '17AF', '17AC', '17AE', '25E', '264', '261', '256', '255', '254', '251', '252', '250', '249', '24C', '24A', '24A', '248', '245', '249', '249', '24A', '247', '24C', '244', '24C', '249', '24E', '24E', '24C', '26C', '2E2', '336', '337', '33B', '337', '33A', '332', '33E', '339', '33A', '33A', '33D', '33E', '341', '340', '344', '347', '344', '344', '352', '35A', '35D', '366', '379', '381', '1186', '1831', '183C', '1840', '184A', '17FA', '17AE', '17BB', '17C2', '17C7', '17CF', '17DB', '17E4', '186E', '18AB', '18B7', '18C2', '18A1', '1837', '1848', '1867', '1864', '1874', '1877', '0', '0', '0', '0', '2', '1AD', '1B1', '1AB', '1A9', '17A7', '12B3', '1944', '0', '0', '0', '0', '0', '0', '0', '2', '2', '0', '2', '2', '7FF', '801', '804', '800', '7FC', '805', '7DE', '6AC', 'CD6', 'CBD', 'C9C', 'C81', 'C66', 'C49', 'C20', 'BDB', 'D2C', 'D54', 'C4C', 'C3E', 'C33', 'C2F', 'C2D', 'C2A', 'C2D', 'C23', 'C23', 'C1E', 'C1B', 'C1A', 'C18', 'C10', 'C11', 'C10', 'C0A', 'C0B', 'C07', 'C07', 'C05', 'C04', 'C03', 'C00', 'BFE', 'C03', 'BED', '0', 'B62', 'B32', 'B2E', 'B20', 'B0D', 'B0C', 'B20', 'B30', 'B3C', 'B7C', 'CC1', 'CC9', 'B0E', 'ACE', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'F74', '886', '0', 'BB9', 'BB2', 'BA4', 'B9A', 'B7A', 'B0E', '936', '871', '876', '876', '86F', '872', '86F', '86F', '86D', '86C', '86A', '865', '861', '86A', '864', '85A', '864', '864', '860', '85C', '859', '865', '860', '862', '85A', '85B', '85F', '85E', '861', '85A', '85D', '858', '863', '85F', '864', '868', '870', '865', '866', '884', '93F', '982', '97D', '977', '96F', '96E', '96F', '96C', '95E', '960', '956', '955', '954', '94B', '948', '944', '8C8', '8D1', '8D4', '8F0', '8E8', '8B0', '88B', '8BC', '8D0', '8D7', '8C6', '8BD', '808', '7EB', '7EC', '7ED', '815', '8A0', '8C1', '8B4', '8BD', '8B1', '8A8', '7F5', '7EA', '7DA', '7D6', '7CC', '7BF', '7B3', '7AD', '79F', '796', '78F', '783', '779', '771', '771', '764', '757', '74D', '745', '743', '734', '72C', '72A', '729', '71D', '715', '711', '70E', '6FE', '6FA', '6F2', '6ED', '6E7', '6DF', '6D9', '6D3', '2', '7CF', '844', '844', '863', '861', '880', '856', '83B', '824', '6D8', '632', '61E', '5FD', '5F7', '5FC', '5F6', '5F9', '5F3', '5F4', '5F1', '5F8', '5F9', '5F8', '5FD', '5FC', '5FF', '600', '603', '606', '605', '606', '609', '60A', '60C', '611', '612', '616', '61C', '61D', '61E', '61A', '624', '623', '624', '62A', '62E', '631', '632', '634', '639', '63A', '642', '643', '646', '649', '64F', '657', '657', '65B', '65D', '664', '667', '66A', '66F', '675', '67E', '682', '68E', '691', '696', '69A', '69D', '69F', '6A0', '6A5', '6A8', '47', '61', '9E', 'BB', 'BA', 'BB', 'B4', 'B6', 'B7', 'B6', 'B7', 'B7', 'BA', 'C1', 'BD', 'BC', 'B9', 'B9', 'BE', 'BD', 'BC', 'BA', 'BB', 'BD', 'C3', 'C2', 'BD', 'BC', 'BE', 'C6', '2', '91', '87', 'B1', '98', 'B3C', 'B32', 'B31', 'B28', 'B1C', 'B13', '11C2', '11A3', '1176', '1180', '1178', 'A8D', '112C', '111F', '1109', 'A49', 'A36', 'A40', 'A43', 'CEA', 'D45', 'D56', 'D6E', 'D87', 'D9B', 'DB5', 'DCD', 'DE5', 'DFE', 'E15', 'E31', 'E4E', 'E66', 'E69', 'E6E', 'E82', '2CD', 'RSSI1', '3F800000', '00000000', 'FFF92230', 'D05', '32B', '0', '0', 'D93', '1308', '1DAC', '2091', '1FAB', '22CA', '246A', '2010', '1329', '1344', '0', '81D', '0', '7FC', '984', '0', '0', '0', '0', 'D07', 'EA0', 'E88', 'F42', '1045', '1162', '1237', '12D8', '14A4', '1628', '1703', '16C8', '1856', '17BB', '181C', '18EC', '19F5', '1A18', '1A60', '1B3A', '1A1F', '1A6B', '1A21', '1997', '1D52', '1ABD', '1AB8', '1A17', '11CF', '0', '18A6', '200A', '1F33', '216B', '1B66', '1641', '1712', '144C', '170B', '2151', '205C', '2475', '294D', '23DF', '268D', '2C41', '26D4', '2321', '2A87', '2C4E', '2A50', '2221', '1A18', '1AA6', '19AD', '1CA2', '1CD0', '1418', '0', '0', '0', '10E2', '181C', '19BE', '19C2', '193B', '18F5', '184B', '1859', '17E2', '1838', '17ED', '194B', '17D2', '18C6', '174C', '176C', '16FA', '1703', '16B7', '17D8', '17AF', '17D5', '184E', '18D2', '17EF', '1553', '2418', '28BC', '9A93', '2655', '2D55', '2E01', '2E2F', '2E8F', '2D92', '2DD5', '2E88', '2D9B', '2E51', '2E3D', '2DE8', '2DEF', '2EBF', '2D73', '2ED9', '2F2B', '3073', '30B0', '3018', '2FCC', '2EF4', '2F33', '2E05', '2E4D', '2F3A', '2FEF', '3135', '32FC', '32BF', '3140', '2FF3', '2FE3', '317F', '30EA', '337B', '3597', '325D', '3103', '30C2', '30E7', '30AE', '2E4F', '2E76', '2F37', '2EBA', '2C51', '2641', '23B6', '2612', '1B61', '140E', '16B0', '16BE', '176D', '16F1', '17DE', '16EC', '1736', '1823', '1794', '17BF', '18C9', '180F', '185F', '184E', '1705', '1758', '1221', '19F8', '1FFA', '204B', '2187', '2052', '21B1', '2088', '2174', '2263', '239E', '2821', '2993', '26CF', '23AA', '2345', '20B2', '209A', '2282', '2240', '22CF', '24CC', '1E4A', '1675', '1564', '138E', '1222', '13BA', '105A', '10F1', 'F69', 'E72', '8DA', '1719', '2D93', '337B', '36E9', '35AA', '31AA', '28AE', '24FC', '24FF', '24A1', '25F9', '290D', '2BCF', '2D05', '2FCB', '3136', '32ED', '326F', '30AC', '2D46', '2B27', '27F2', '263D', '23C7', '21D6', '1E5E', '1ED8', '1E42', '0', '236A', '2DA8', '3170', '33A4', '333C', '3380', '33CE', '3245', '31A0', '321F', '2955', '1E98', '266C', '2244', '2BB7', '321F', '324D', '330A', '2FE2', '2E6C', '2D33', '2CA6', '2C19', '2CBB', '2E15', '2CE9', '2D7D', '2ED9', '2F5F', '2E9A', '2F8A', '2E21', '2E48', '2D3C', '2C67', '2DC6', '2D0F', '2D4F', '2E39', '2C7D', '2847', '1735', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'A24', '0', '0', '1FF5', '25BB', '27AC', '274A', '2688', '26F1', '273D', '27EC', '2CC3', '2C26', '292D', '2878', '2724', '27CD', '283F', '295F', '2889', '2B7B', '2BF5', '2C58', '2A16', '2A19', '2B1A', '2A05', '2A0B', '29B3', '2AA1', '2D8C', '2D69', '2CF8', '2BE2', '2C80', '2CDB', '2D2E', '2D8F', '2DED', '3081', '303C', '2EAD', '2B41', '2991', '2ACB', '284A', '22F0', '211D', '1EF4', '1DE2', '1FA0', '1E6A', '15C7', '1229', '1128', 'BB7', 'CCE', '118A', '1FAF', '1B7F', '1ADE', '1EEC', '1ED5', '1D80', '1B70', '2407', '20DB', '1E2E', '20DB', '20B6', '21F5', '22D9', '240E', '254F', '252D', '27C0', '28D4', '2AB8', '2BB0', '2C9D', '2EB0', '2F50', '2F2B', '2E97', '2F60', '2E34', '335B', '370F', '38E6', '38C6', '3716', '36D3', '34C2', '3868', '39CD', '39BC', '3954', '3A0B', '38CA', '3A00', '399C', '38AA', '37FF', '381E', '387A', '38F1', '3849', '37CB', '371C', '3611', '34CF', '359F', '347F', '32FF', '31D8', '3056', '2B2D', '2039', '1ED4', '2007', '1F49', '1F3A', '1CFD', '1E49', '1E42', '1FF7', '1CD3', '1A6E', '1AD6', '1AAA', '1CD7', '1F68', '1F63', '1E55', '164A', 'C52', 'C4F', 'B26', 'DBC', 'BF2', '9A8', '0', '0', '0', '0', '0', '1564', '148F', '1CFE', '24F1', 'D90', 'CB4', '692', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1937', '1CD1', '211B', '224F', '178D', 'DB4', 'DC6', '1FA8', '24B8', '2608', '2548', '254D', '2481', '24B5', '21CF', '14C4', 'DD9', '188B', '14A8', '1B17', '1BD7', '1BC8', '1B74', '1CA9', '1DC4', '1CDE', '1C08', '1D7E', '1DD3', '1DD8', '1DF4', '1E91', '1E50', '1E6C', '1DF1', '1EA2', '1E5D', '1F11', '20C7', '207C', '1FC6', '1F6E', '1FBD', '1EF2', '1766', '0', 'A28', '1E7C', '24BB', '260C', '268C', '2731', '2929', '2822', '25FA', '1E2A', '17D2', '19EB', '1294', '10FD', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'C0E', '19F2', '0', '253B', '28D7', '288C', '296C', '28CB', '2592', 'E9B', '256F', '275D', '28A1', '28E0', '2A65', '2A4D', '2B2A', '2C2E', '2D2C', '2DFC', '2DEB', '2EE2', '3138', '320C', '3259', '350E', '3717', '3805', '3910', '3AC0', '805D', '8082', '80E3', '80B2', '80FC', '80CB', '8076', '8020', '3A87', '3855', '364E', '363A', '33CC', '32FA', '3245', '3118', '2EFD', '2DDD', '275D', '2824', '2CF4', '2CEF', '2D1B', '2C4B', '2DB9', '2D9D', '2E5B', '2D5A', '2E21', '2C34', '2DAB', '2DF2', '2D3A', '2D8A', '2ABF', '1C98', '1C96', '1B22', '1F1E', '219F', '19A6', '171F', '1D54', '2940', '2F3D', '2D84', '2A91', '1F79', '224B', '251D', '2594', '2351', '29EA', '2FAA', '2DD4', '2FBA', '2C94', '1FFA', '1304', '1694', '1644', '16A2', '16F2', '15DE', '17A5', '1757', '18C2', '17D9', '18CE', '1842', '19A2', '1993', '19A9', '1822', '195B', '1925', '1B11', '1946', '1B0C', '1B28', '1AB1', '1A60', '1A86', '1BE9', '1B94', '1B22', '19E2', '1BE8', '1B78', '1AEF', '1AB7', '1C65', '1B5F', '1820', '0', 'DC4', '244C', '28BB', '2A10', '2777', '249E', '2320', '2138', '1A0C', '197B', '25B0', '252F', '2A64', '2A34', '2AB4', '293E', '2C6B', '29B8', '2996', '2864', '29A5', '29BA', '28BB', '2A32', '2976', '2935', '2902', '294A', '2984', '28C8', '292B', '285E', '2893', '297A', '2892', '288B', '28A0', '2978', '2963', '2956', '2838', '28FB', '2823', '2766', '284A', '28E3', '283A', '282B', '2715', '2831', '26D0', '285C', '276D', '27ED', '2797', '274F', '27B6', '268A', '25EC', '2707', '26C0', '261A', '2553', '2582', '255F', '25F1', '247C', '261B', '2498', '2525', '22E9', '21DB', '2142', '1FC5', '2045', '1F62', '1FE6', '1DB1', '1880', '161F', '16AA', '1A2E', '1C22', '1CF6', '1DAA', '1E4E', '1EBE', '1DF9', '1C47', '1DB9', '1E7B', '1F85', '1FA6', '2204', '2257', '2350', '2455', '23DE', '24A4', '2491', '2510', '2400', '2171', '1EBE', '1B20', '1637', '0', '26D2', '1FAF', '1A1A', '165A', '1730', '1ED7', '1DEE', '14ED', 'C8A', 'C0D', '904', '80F', '9D9', '999', 'A37', 'B4C', 'B04', '90B', '8C4', '1063', '15A7', '1815', '1289', '14F3', '2321', '222D', '238A', '2500', '23C2', '2464', '2490', '2327', '2416', '2433', '24D1', '22FD', '22DB', '2322', '2196', '1EF4', '1F97', '0', '0', '0', '0', '0', '0']

    elif a == 2:

        telegram = "sRA LMDscandata 1 1 1078AAA 0 0 BFD BFF CFACE0D CFAE156 0 0 1 0 0 5DC A2 0 1 DIST1 3F800000 00000000 FFF92230 D05 32B 24B 257 260 277 287 28D 296 29A 2A2 2A1 28E 280 284 28C 287 280 292 29A 2A1 2A0 29C 29D 29C 297 295 294 284 284 276 274 278 277 279 28C 28B 28A 28F 29A 287 279 280 285 284 27F 27F 284 278 27A 275 273 272 25B 22C 221 21C 218 21A 212 216 21D 23E 25D 25F 25B 24E 254 252 256 24B 243 22D 21A 20F 211 213 20F 216 224 234 241 242 241 242 23B 241 23A 230 235 22B 21F 218 206 1EE 1B8 186 17B 17A 173 173 171 171 16A 16B 16D 16B 16B 168 16D 168 168 167 165 166 165 168 167 165 161 162 163 15F 164 15F 15E 157 15E 158 158 154 153 156 154 151 156 15C 18C 1D7 1ED 1F8 20B 208 20D 214 215 21C 21C 21B 225 224 22A 224 228 229 229 22A 22D 225 22A 220 225 229 225 226 22C 228 22C 22B 229 22A 21A 219 20E 204 205 1FD 204 204 203 200 205 205 205 205 205 205 206 20B 207 20C 20E 212 226 27A 2B0 2AE 2AC 2B0 2B7 2B5 2C3 2CE 2CE 2CC 2DA 2D9 2DF 2E1 2E3 2E2 2E3 2E8 2EC 2EC 2F3 2F5 2FA 2FA 2FA 2FD 306 305 301 305 310 30C 313 318 31D 318 31B 324 322 31D 32A 32B 32F 331 334 336 339 335 339 340 345 34A 34A 34A 31C 270 243 23D 246 247 24C 24B 245 241 249 24D 24E 249 242 254 24E 254 258 250 254 25C 257 250 252 255 255 255 256 258 25C 25B 25A 260 25B 25E 25C 262 260 263 264 266 268 26A 26A 26B 26C 26D 270 26F 26E 271 273 272 272 278 277 27C 27A 27B 281 280 27F 282 283 280 283 288 288 288 28D 28B 290 291 293 293 297 299 29B 29B 29D 2A4 2A1 2A6 2A8 2A8 2A9 2AD 2AF 2B2 2B2 2B8 2B5 2BA 2BC 2BE 2C3 2C6 2C7 2C9 2C8 2D0 2D3 2D1 2D5 2D9 2DB 2DB 2E3 2E0 2E5 2EC 2ED 2EE 2F3 2F4 2FD 2FD 300 301 2FE 2F9 2EE 674 655 65F 654 667 673 67E 680 688 69C 6B4 0 393 38B 0 65A 65E 66A 674 674 67D 686 689 66E 669 6AC 79B 7FE 813 80E 817 80F 810 80F 81B 811 7F7 7CA 7D3 7F8 7D2 7E3 7FB 6A8 4BB 412 4D0 583 58B 592 5F4 6E2 6F0 698 6B4 6BA 67A 643 625 635 674 6B1 6B3 6A9 67D 6A3 6B1 694 675 684 6AD 6CD 669 66B 7FC 859 863 862 865 85C 700 6D0 6E5 6E2 70B 716 717 714 705 703 6DD 2 2 62B 5F5 5E9 5EE 5F0 5F7 D22 0 0 0 0 0 0 644 640 639 63A 639 646 643 651 657 65A 693 7A7 7CA 7DB 7E2 7EA 7EF 7FD 807 811 815 824 82C 834 83D 84A 852 860 86B 876 879 889 89A 8A3 8B0 8BE 8CC 8D9 8ED 8F4 8F1 8EA 900 916 926 926 92E 936 93C 943 94E 94D 959 962 961 96F 972 985 98A 98C 993 99B 9A6 9B1 9BA 9BF 9C6 9D8 9D9 9EA 9F2 9FC 9FB 9E5 9CA 9C7 9CB 9B7 9AD 9A6 9A7 9B5 9C7 9DA 9EC 9FF A14 A1F A37 0 0 0 0 0 0 0 1139 0 0 0 EB9 ED3 EF4 F1B F3C F5A 8BA 8B3 8BD FCB 1007 1055 1076 1097 1060 1044 1049 104E 105B 1069 1068 1075 1076 1086 108F 10AE 3E4 374 2F6 306 2F7 2FE 301 2FA 2F0 2F3 308 30A 309 308 314 321 37C 3BF 3BC 3BD 3C0 3C1 3BA 3C3 3BB 3C2 3C3 3C1 3C7 3C0 3C2 3BC 3BF 3C5 3CB 3C3 3C9 3C5 3C7 3CD 3BE 3C1 3B1 3B9 3BC 3C0 3BE 3C3 3C7 3CC 3CE 3DE 3DF 3DB 3E3 3EA 3F5 401 400 40B 424 43E 44E 2056 ED3 EC2 EBD EBA EBA EBD EBA EB8 EB5 EB8 EBA 805 7B8 7A1 794 78B 780 774 76B 767 761 762 763 779 7B0 7F0 7FA 803 812 81B 81D 819 8AE 86C 117A 1184 1184 118E 118E 1197 1195 1193 1191 1197 119B 11AB 11AD 11A3 11A5 11B3 11C7 11F5 234E 11FE 602 600 5FF 5FF 60A 0 0 0 0 0 0 0 0 0 7F8 7AA D2C D23 D2B 0 0 0 1348 1327 1310 1308 B6F B8D BD0 CCA CEC CF1 D0A 847 85E 83F 82B 818 807 7F9 801 80A 2 870 853 83B 81D 814 7E2 7C3 7BC 7BF 380 391 390 375 37A 37C A19 0 2 2 2 2DA 33A 34A 34E 346 982 AC 86 29B 295 9B 7B 73 72 77 72 70 73 71 73 74 77 72 71 71 77 79 79 0 0 1 7 Daniyal 0 0 0"

    if type(telegram) != list:
        telegram = telegram.split(' ')

    return telegram

################################################################
#   ERRORS

error_codes=[
    "Sopas_Ok",
    "Sopas_Error_METHODIN_ACCESSDENIED",
    "Sopas_Error_METHODIN_UNKNOWNINDEX",
    "Sopas_Error_VARIABLE_UNKNOWNINDEX",
    "Sopas_Error_LOCALCONDITIONFAILED",
    "Sopas_Error_INVALID_DATA",
    "Sopas_Error_UNKNOWN_ERROR",
    "Sopas_Error_BUFFER_OVERFLOW",
    "Sopas_Error_BUFFER_UNDERFLOW",
    "Sopas_Error_ERROR_UNKNOWN_TYPE",
    "Sopas_Error_VARIABLE_WRITE_ACCESSDENIED",
    "Sopas_Error_UNKNOWN_CMD_FOR_NAMESERVER",
    "Sopas_Error_UNKNOWN_COLA_COMMAND",
    "Sopas_Error_METHODIN_SERVER_BUSY",
    "Sopas_Error_FLEX_OUT_OF_BOUNDS",
    "Sopas_Error_EVENTREG_UNKNOWNINDEX",
    "Sopas_Error_COLA_A_VALUE_OVERFLOW",
    "Sopas_Error_COLA_A_INVALID_CHARACTER",
    "Sopas_Error_OSAI_NO_MESSAGE",
    "Sopas_Error_OSAI_NO_ANSWER_MESSAGE",
    "Sopas_Error_INTERNAL",
    "Sopas_Error_HubAddressCorrupted",
    "Sopas_Error_HubAddressDecoding",
    "Sopas_Error_HubAddressAddressExceeded",
    "Sopas_Error_HubAddressBlankExpected",
    "Sopas_Error_AsyncMethodsAreSuppressed",
    "Sopas_Error_ComplexArraysNotSupported"
    ]


error_descriptions = {
    "Sopas_Error_METHODIN_ACCESSDENIED": "Wrong userlevel, access to method not allowed",
    "Sopas_Error_METHODIN_UNKNOWNINDEX": "Trying to access a method with an unknown Sopas index",
    "Sopas_Error_scandatacfgVARIABLE_UNKNOWNINDEX": "Trying to access a variable with an unknown Sopas index",
    "Sopas_Error_LOCALCONDITIONFAILED": "Local condition violated, e.g. giving a value that exceeds the minimum or maximum allowed value for this variable",
    "Sopas_Error_INVALID_DATA": "Invalid data given for variable, this errorcode is deprecated (is not used anymore).",
    "Sopas_Error_UNKNOWN_ERROR": "An error with unknown reason occurred, this errorcode is deprecated.",
    "Sopas_Error_BUFFER_OVERFLOW": "The communication buffer was too small for the amount of data that should be serialised.",
    "Sopas_Error_BUFFER_UNDERFLOW": "More data was expected, the allocated buffer could not be filled.",
    "Sopas_Error_ERROR_UNKNOWN_TYPE": "The variable that shall be serialised has an unknown type. This can only happen when there are variables in the firmware of the device that do not exist in the released description of the device. This should never happen.",
    "Sopas_Error_VARIABLE_WRITE_ACCESSDENIED": "It is not allowed to write values to this variable. Probably the variable is defined as read-only.",
    "Sopas_Error_UNKNOWN_CMD_FOR_NAMESERVER": "When using names instead of indices, a command was issued that the nameserver does not understand.",
    "Sopas_Error_UNKNOWN_COLA_COMMAND": "The CoLa protocol specification does not define the given command, command is unknown.",
    "Sopas_Error_METHODIN_SERVER_BUSY": "It is not possible to issue more than one command at a time to an SRT device.",
    "Sopas_Error_FLEX_OUT_OF_BOUNDS": "An dataay was accessed over its maximum length.",
    "Sopas_Error_EVENTREG_UNKNOWNINDEX": "The event you wanted to register for does not exist, the index is unknown.",
    "Sopas_Error_COLA_A_VALUE_OVERFLOW": "The value does not fit into the value field, it is too large.",
    "Sopas_Error_COLA_A_INVALID_CHARACTER": "Character is unknown, probably not alphanumeric.",
    "Sopas_Error_OSAI_NO_MESSAGE": "Only when using SRTOS in the firmware and distributed variables this error can occur. It is an indication that no operating system message could be created. This happens when trying to GET a variable.",
    "Sopas_Error_OSAI_NO_ANSWER_MESSAGE": "This is the same as \"Sopas_Error_OSAI_NO_MESSAGE\" with the difference that it is thrown when trying to PUT a variable.",
    "Sopas_Error_INTERNAL": "Internal error in the firmware, problably a pointer to a parameter was null.",
    "Sopas_Error_HubAddressCorrupted": "The Sopas Hubaddress is either too short or too long.",
    "Sopas_Error_HubAddressDecoding": "The Sopas Hubaddress is invalid, it can not be decoded (Syntax).",
    "Sopas_Error_HubAddressAddressExceeded": "Too many hubs in the address",
    "Sopas_Error_HubAddressBlankExpected": "When parsing a HubAddress an expected blank was not found. The HubAddress is not valid.",
    "Sopas_Error_AsyncMethodsAreSuppressed": "An asynchronous method call was made although the device was built with \“AsyncMethodsSuppressed\”. This is an internal error that should never happen in a released device.",
    "Sopas_Error_ComplexArraysNotSupported": "Device was built with „ComplexArraysSuppressed“ because the compiler does not allow recursions. But now a complex dataay was found. This is an internal error that should never happen in a released device."
    }

timeout = 500

if demo != True:

    lidar = usb.core.find(idVendor=0x19a2, idProduct=0x5001)

    if lidar is None:
        print('LIDAR Device not found!')
        exit()


############################################
#   Basic Settings

def remove_control_characters(s):
    s = "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")
    return s

def dec_to_ascii(s):
    s = "".join(chr(x) for x in s)
    return s

def hex_to_dec(i):
    i = [ int(x,16) for x in i ]
    return i


def hex_to_meters(i):
    i = [ int(x,16)/1000 for x in i ]
    return i

def uint32(i):
    i = struct.unpack('>i', bytes.fromhex(i))[0]
    return i

def check_error(s):
    if s[0:3] == "sFA":
        error_code = error_codes[int(s[1],16)]
        error_description = error_descriptions[error_code]
        return [error_code,error_description]
    else:
        return s

def parse_str(d):
    if d == None:
        return d
    else:
        d = d.split()
        d = d[len(d)-1]
        return d

## LIDAR FUNCTIONS ##

def read():
    arr = lidar.read(1|usb.ENDPOINT_IN,65535,timeout=100)
    arr = "".join([chr(x) for x in arr[1:-1]])
    arr = check_error(arr)
    return arr

def send(cmd):
    lidar.write(2|usb.ENDPOINT_OUT,"\x02"+cmd+"\x03\0",0)
######################

def firmwarev():
    send('sRN FirmwareVersion')
    answer = read()
    answer = answer.split()
    answer = answer[-1]
    return answer

def deviceident():
    send('sRI0')
    answer = read()
    answer = answer.split()
    answer = answer[3] + ' ' + answer[4] + ' ' + answer[5]
    return answer

def setaccessmode(user="03",password="F4724744"):
    send('sMN SetAccessMode '+user+" "+password)
    answer = read()
    if answer == "sAN SetAccessMode 1":
        return 0
    else:
        return answer

def scancfg():   # Read for frequency and angular resolution
    # Request Read Command
    # sRN LMPscancfg
    send('sRN LMPscancfg')
    answer = read()
    answer = answer.split()

    if len(answer) == 7:
        scan_freq = int(answer[2],16)/100
        sectors = int(answer[3],16)
        ang_res = int(answer[4],16)/10000   # Manual says uint_32?
        start_ang = int(answer[5],32)/10000
        stop_ang = int(answer[6],32)/10000
        return [scan_freq,sectors,ang_res,start_ang,stop_ang]

    else:
        return answer

def startmeas():   # Start measurement
    # sMN LMCstartmeas
    send('sMN LMCstartmeas')
    answer = read()
    if answer == "sAN LMCstartmeas 0":
        return 0
    else:
        return answer
    #   Start the laser and (unless in Standby mode) the motor of the the device

def stopmeas():   # Stop measurement
    # sMN LMCstopmeas
    send('sMN LMCstopmeas')
    answer = read()
    if answer == "sAN LMCstopmeas 0":
        return 0
    else:
        return answer
    #   Shut off the laser and stop the motor of the the device

def loadfacdef():   # Load factory defaults
    # sMN mSCloadfacdef
    send('sMN mSCloadfacdef')
    answer = read()
    if answer == "sAN mSCloadfacdef":
        return 0
    else:
        return answer

def loadappdef():    # Load application defaults
    # sMN mSCloadappdef
    send('sMN mSCloadappdef')
    answer = read()
    return answer

def checkpassword(user,password):    # Check password
    # sMN CheckPassword 03 19 20 E4 C9
    send('sMN CheckPassword '+user+' '+password)
    answer = read()
    return answer
    # sAN CheckPassword  1

def reboot():    # Reboot device
    # sMN mSCreboot
    send('sMN mSCreboot')#
    answer = read()
    if answer == "sAN mSCreboot":
        return 0
    else:
        return answer
    # sAN mSCreboot

def writeall():    # Save parameters permanently
    # sMN mEEwriteall
    send('sMN mEEwriteall')
    answer = read()
    return answer
    # sAN mEEwriteall 1

def run():    # Set to run
    # sMN Run
    send('sMN Run')
    answer = read()
    if answer == "sAN Run 1":
        return 0
    else:
        return answer
    # sAN Run 1

#####################################################################

#   Measurement output telegram


#DOES NOT WORK YET
def scandatacfg(channel='01 00', rem_ang=1, res=1, unit=0, enc='00 00', pos=0, name=0, comment=0, time=0, out_rate='+1'):    # Configure the data content for the scan
    # sWN LMDscandatacfg 01 00 1 1 0 00 00 0 0 0 0 +1
    # sWN LMDscandatacfg 01 00 1 1 0 00 00 0  0 0 +10
    # sWN LMDscandatacfg 02 0 0 1 0 01 0 0 0 0 0 +10
    send('sWN LMDscandatacfg '+str(channel)+' '+str(rem_ang)+' '+str(res)+' '+str(unit)+' '+str(enc)+' '+str(pos)+' '+str(name)+' '+str(comment)+' '+str(time)+' '+str(out_rate))
    answer = read()
    if answer == "sWA LMDscandatacfg":
        return 0
    else:
        return answer

    # sWA LMDscandatacfg

def outputRange():    # Configure measurement angle of the scandata for output
    # sWN LMPoutputRange 1 1388 0 DBBA0
    send('sWN LMPoutputRange')
    answer = read()
    return answer
    # sWA LMPoutputRange

def outputRange():    # Read for actual output range
    # sRN LMPoutputRange
    send('sRN LMPoutputRange')
    answer = read()
    return answer
    # sRA LMPoutputRange 1 1388 FFF92230 225510

def scan(raw=False):    # Get LIDAR Data

    send('sRN LMDscandata')
    raw_data = read()
    data = raw_data

    if raw == False:

        scan.dist_start = None
        scan.rssi_start = None

        data = data.split()

        for index, item in enumerate(data):
            if "DIST" in item and scan.dist_start == None:
                scan.dist_start = index

            if "RSSI" in item:
                scan.rssi_start = index

        scan.telegram_len = len(data)
        scan.cmd_type =         data[0]
        scan.cmd =              data[1]
        scan.version =      int(data[2],16)
        scan.device_num =   int(data[3],16)
        scan.serial_num =   int(data[4],16)
        scan.device_stat =  int(data[6],8)
        scan.telegram_cnt = int(data[7],16)
        scan.scan_cnt =     int(data[8],16)
        scan.uptime =       int(data[9],32)
        scan.trans_time =   int(data[10],32)
        scan.input_stat =   int(data[12],32)
        scan.output_stat =  int(data[14],8)
        scan.layer_ang =    int(data[15],16)
        scan.scan_freq =    int(data[16],32)/100
        scan.meas_freq =    int(data[17],16)/100   # Math may not be right
        scan.enc_amount =   int(data[18],16)

        scan.num_16bit_chan = int(data[19],16)

        if scan.dist_start != None:

            scan.dist_label = data[20]
            scan.dist_scale_fact = int(data[scan.dist_start+1],16)
            scan.dist_scale_fact_offset = int(data[scan.dist_start+2],16)
            scan.dist_start_ang = uint32(data[scan.dist_start+3])/10000
            scan.dist_angle_res = int(data[scan.dist_start+4],16)/10000
            scan.dist_data_amnt = int(data[scan.dist_start+5],16)
            scan.dist_end = (scan.dist_start+6) + scan.dist_data_amnt
            scan.distances = hex_to_meters(data[scan.dist_start+6:scan.dist_end])
            scan.raw_distances = " ".join(data[scan.dist_start+6:scan.dist_end])

        if scan.rssi_start != None:

            scan.rssi_label = data[20]
            scan.rssi_scale_fact = int(data[scan.rssi_start+1],16)
            scan.rssi_scale_fact_offset = int(data[scan.rssi_start+2],16)
            scan.rssi_start_ang = uint32(data[scan.rssi_start+3])/10000
            scan.rssi_angle_res = int(data[scan.rssi_start+4],16)/10000
            scan.rssi_data_amnt = int(data[scan.rssi_start+5],16)
            scan.rssi_end = (scan.rssi_start+6) + scan.rssi_data_amnt
            scan.rssi = data[scan.rssi_start+6:scan.rssi_end]

        return raw_data

# LMDscandata - reserved values PAGE 80

#####################################################################
#   Filter

def particle():    # Set particle filter
    # sWN LFPparticle 1 +500
    send('sWN LFPparticle')
    answer = read()
    return answer
    # sWA LFPparticle

def meanfilter(status_code=0,number_of_scans="+10"):    # Set mean filter
    # sWN LFPmeanfilter 1 +10 0
    send('sWN LFPmeanfilter '+status_code+' '+number_of_scans+' 0')
    answer = read()
    return answer
    # sWA LFPmeanfilter


#####################################################################
#   Outputs



def outputstate():    # Read state of the outputs
    # sRN LIDoutputstate
    send('sRN LIDoutputstate')

def eventoutputstate(state):    # Send outputstate by event
    send('sEN LIDoutputstate '+str(state))
    answer = read()
    return answer

def setoutput():    # Set output state
    # sMN mDOSetOutput 1 1
    send('sMN mDOSetOutput')
    answer = read()
    return answer
    # sAN mDOSetOutput 1
#####################################################################
#   Inputs

def debtim():    # Set debouncing time for input x
    # sWN DI3DebTim +10
    send('sWN DI3DebTim')
    answer = read()
    return answer
    # sWA DI3DebTim

def deviceident():    # Read device ident
    # sRN DeviceIdent
    send('sRN DeviceIdent')
    answer = read()
    answer = answer.split()
    answer = answer[3] + ' ' + answer[4] + ' ' + answer[5]
    return answer
    # sRA DeviceIdent 10 LMS10x_FieldEval 10 V1.36-21.10.2010

def devicestate():    # Read device state
    # sRN SCdevicestate
    send('sRN SCdevicestate')
    answer = read()
    return answer
    # sRA SCdevicestate 0

def ornr():    # Read device information
    # sRN DIornr
    send('sRN DIornr')
    answer = read()
    return answer
    # sRA DIornr 1071419

def devicetype():    # Device type
    # sRN DItype
    send('sRN DItype')
    answer = read()
    return answer
    # sRA DItype E TIM561-2050101

def oprh():    # Read operating hours
    # sRN ODoprh
    send('sRN ODoprh')
    answer = read()
    return answer
    # sRA ODoprh 2DC8B

def pwrc():    # Read power on counter
    # sRN ODpwrc
    send('sRN ODpwrc')
    answer = read()
    return answer
    # sRA ODpwrc 752D

def setLocationName(name):    # Set device name
    # sWN LocationName +13 OutdoorDevice
    name = " " + name
    string = 'sWN LocationName +'+str(len(name)-1)+name
    send(string)
    answer = read()
    return answer
    # sWA LocationName

def readLocationName():    # Read for device name
    # sRN LocationName
    send('sRN LocationName')
    answer = read()
    answer = parse_str(answer)
    return answer
    # sRA LocationName D OutdoorDevice

def rstoutpcnt():    # Reset output counter
    # sMN LIDrstoutpcnt
    send('sMN LIDrstoutpcnt')
    answer = read()
#    answer = parse_str(answer)
    return answer
    # sAN LIDrstoutpcnt 0
