import pymysql
import pickle


def get_cctv_list():
    with open('cctv_list.p', 'rb') as f:
        cctv_list = pickle.load(f)
    return cctv_list


def get_conn():
    return pymysql.connect(
        host='localhost',
        user='soma',
        password='soma123',
        db='cctv_map',
        charset='utf8')


if __name__ == '__main__':
    conn = get_conn()
    cur = conn.cursor()
    cctv_list = get_cctv_list()
    for i in range(len(cctv_list)):
        cctv = cctv_list[i]
        for key in cctv.keys():
            cctv[key] = cctv[key].strip()
            if cctv[key] == 'null':
                continue
            elif cctv[key] == '':
                cctv[key] = 'null'
            elif key == 'installationYymm':
                cctv[key] = f'"{cctv[key]}-01"'
            elif key not in ['cctvNumber', 'cctvPixel', 'cstdyDay', 'latitude', 'longitude']:
                cctv[key] = f'"{cctv[key]}"'
        sql = 'INSERT INTO CCTV ('
        sql += ', '.join(cctv.keys())
        sql += ')'
        sql += ' VALUES ('
        sql += ', '.join(cctv.values())
        sql += ')'
        try:
            cur.execute(sql)
            conn.commit()
        except:
            print("error from", i)
    conn.close()