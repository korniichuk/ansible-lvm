select
               a.tablespace_name,
               round(SUM(decode(b.maxextend, null, A.BYTES/(1024*1024*1024),
               b.maxextend*8192/(1024*1024*1024)))) MAX_GB,
               round(100*(SUM(a.bytes)/(1024*1024*1024) -
               round(c.Free/1024/1024/1024))/(SUM(decode(b.maxextend, null, A.BYTES/(1024*1024*1024),
               b.maxextend*8192/(1024*1024*1024))))) USED_PCT
from
               dba_data_files a,
               sys.filext$ b,
               (SELECT
                              d.tablespace_name ,sum(nvl(c.bytes,0)) Free
               FROM
                              dba_tablespaces d,
                              DBA_FREE_SPACE c
               WHERE
                              d.tablespace_name = c.tablespace_name(+)
                              group by d.tablespace_name) c
WHERE
               a.file_id = b.file#(+)
               and a.tablespace_name = c.tablespace_name
               and a.tablespace_name = 'DEMO'
               GROUP BY a.tablespace_name, c.FREE/1024
/
exit;
