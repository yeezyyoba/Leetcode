with ranked as (
    select
        e.id,
        e.name,
        e.departmentId,
        e.salary,
        DENSE_RANK() over (
            partition by e.departmentId
            order by e.salary desc
        ) as rnk
    from Employee e
)
select
    d.name  as Department,
    r.name  as Employee,
    r.salary as Salary
from ranked r
join Department d on r.departmentId = d.id
where r.rnk <= 3;
